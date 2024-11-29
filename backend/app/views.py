#from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializerz import RegisterSerializer
from django.http import JsonResponse
from django.middleware.csrf import get_token
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate , get_user_model
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from rest_framework_simplejwt.tokens import RefreshToken


class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
def get_csrf_token(request):
    return JsonResponse({'csrfToken': get_token(request)})

@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')

        # Verifică dacă toate câmpurile sunt completate
        if not username or not email or not password:
            return Response({'message': 'All fields are required!'}, status=status.HTTP_400_BAD_REQUEST)

        # Verifică dacă email-ul este valid
        try:
            validate_email(email)
        except ValidationError:
            return Response({'message': 'Invalid email format!'}, status=status.HTTP_400_BAD_REQUEST)

        # Verifică dacă utilizatorul există deja
        if User.objects.filter(email=email).exists():
            return Response({'message': 'Email is already taken!'}, status=status.HTTP_400_BAD_REQUEST)

        # Validare parolă (exemplu: minim 8 caractere)
        if len(password) < 8:
            return Response({'message': 'Password must be at least 8 characters long!'}, status=status.HTTP_400_BAD_REQUEST)

        # Crează utilizatorul
        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            return Response({'message': 'User registered successfully!'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'message': f"Error: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login(request):
    email = request.data.get('email')  # Obține email-ul din cerere
    password = request.data.get('password')  # Obține parola din cerere

    # Verifică dacă datele sunt complete
    if not email or not password:
        return Response({'message': 'Both email and password are required!'}, status=status.HTTP_400_BAD_REQUEST)

    # Găsim utilizatorul pe baza email-ului
    from django.contrib.auth.models import User
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return Response({'message': 'User not found!'}, status=status.HTTP_404_NOT_FOUND)

    # Autentifică utilizatorul cu username (nume de utilizator) și parolă
    user = authenticate(request, username=user.username, password=password)

    if user is not None:
        # Dacă autentificarea este validă, generăm token-urile
        refresh = RefreshToken.for_user(user)
        return Response({
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }, status=status.HTTP_200_OK)
    else:
        # Dacă autentificarea eșuează
        return Response({'message': 'Invalid credentials!'}, status=status.HTTP_401_UNAUTHORIZED)





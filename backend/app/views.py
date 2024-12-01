#from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializerz import RegisterSerializer
from django.http import JsonResponse
from django.middleware.csrf import get_token
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate ,logout
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import ensure_csrf_cookie  ,csrf_protect , csrf_exempt


class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@ensure_csrf_cookie
def get_csrf_token(request):
    csrf_token = get_token(request)
   # print(f"CSRF TOKEN  : {csrf_token}")
    return JsonResponse({'csrfToken': csrf_token})

@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')
        if not username or not email or not password:
            return Response({'message': 'All fields are required!'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            validate_email(email)
        except ValidationError:
            return Response({'message': 'Invalid email format!'}, status=status.HTTP_400_BAD_REQUEST)
        if User.objects.filter(email=email).exists():
            return Response({'message': 'Email is already taken!'}, status=status.HTTP_400_BAD_REQUEST)
        if len(password) < 8:
            return Response({'message': 'Password must be at least 8 characters long!'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            return Response({'message': 'User registered successfully!'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'message': f"Error: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)

@csrf_protect
@api_view(['POST'])
def login(request):
    email = request.data.get('email')  
    password = request.data.get('password')  
    if not email or not password:
        return Response({'message': 'Both email and password are required!'}, status=status.HTTP_400_BAD_REQUEST)
    from django.contrib.auth.models import User
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return Response({'message': 'User not found!'}, status=status.HTTP_404_NOT_FOUND)

    user = authenticate(request, username=user.username, password=password)

    if user is not None:

        refresh = RefreshToken.for_user(user)
        return Response({
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }, status=status.HTTP_200_OK)
    else:

        return Response({'message': 'Invalid credentials!'}, status=status.HTTP_401_UNAUTHORIZED)

@csrf_exempt   
@api_view(['POST'])
def logout(request):
   # if request.user.is_authenticated:
       # request.auth.delete()  # Șterge tokenul curent
       # response = Response({'message': 'Logged out successfully'}, status=status.HTTP_200_OK)
      #  response.delete_cookie('access_token')  # Șterge cookie-ul JWT de pe client
       # response.delete_cookie('refresh_token')  # Dacă folosești și refresh token

     #   return Response({'message': 'Logged out successfully'}, status=status.HTTP_200_OK)
       # return response
  #  else:
    #    return Response({'error': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)
    if request.method == "POST":
        logout(request)
        response = Response({'message': 'Logged out successfully'}, status=status.HTTP_200_OK)
        response.delete_cookie('access_token')  # Șterge cookie-ul JWT de pe client
        response.delete_cookie('refresh_token')  # Dacă folosești și refresh token
        return response
    else:
        return JsonResponse({'message': 'Invalid request request.'} , status=status.HTTP_405_METHOD_NOT_ALLOWED)


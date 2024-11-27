#from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializerz import RegisterSerializer
from django.http import JsonResponse
from django.middleware.csrf import get_token
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

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
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')

    user = authenticate(username=email, password=password)

    if user is not None:
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})
    else:
        return Response({'error': 'Invalid credentials'}, status=400)
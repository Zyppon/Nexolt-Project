from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User

#from .models import Message


#class MessageSerializer(serializers.ModelSerializer):
   # class Meta:
       # model = Message
      #  fields = ['id', 'content', 'created_at']

class RegisterSerializer(serializers.ModelSerializer):
    password  = serializers.CharField(write_only= True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self , validated_data):
            user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
            return user
    

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        # Verificăm dacă utilizatorul există în baza de date
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid credentials.")

        # Autentificăm utilizatorul folosind email-ul și parola
        user = authenticate(username=email, password=password)
        if not user:
            raise serializers.ValidationError("Invalid credentials.")

        # Generăm token-ul JWT
        refresh = RefreshToken.for_user(user)
        return {
            'access': str(refresh.access_token),
        }
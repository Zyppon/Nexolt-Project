from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Message
from .serializerz import MessageSerializer



class MessageListView(APIView):
    def get(self, request):
        messages = Message.objects.all()
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

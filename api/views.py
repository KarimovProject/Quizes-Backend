

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated


from .serializers import QuizSerializer, QuestionSerializer, OptionSerializer, UserSerializer,ResultSerializer, ResultDetailSerializer, TopicSerializer
# Create your views here.

from .models import Quiz, Question, Option,Topic, User, Result, Result_detail

# View for post all quiz

class Createquiz(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request:Request):
        data = request.data
        serializer = QuizSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class CreateTopic(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request:Request):
        data = request.data
        serializer = TopicSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class CreateQuestion(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request:Request):
        data = request.data
        serializer = QuestionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class CreateOption(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request:Request):
        data = request.data
        serializer = OptionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
class CreateUser(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request:Request):
        data = request.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class CreateResult(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request:Request):
        data = request.data
        serializer = ResultSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class CreateResultDetail(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request:Request):
        data = request.data
        serializer = ResultDetailSerializer(data=data)
        if serializer.is_valid():
            serializer.save
            return Response(serializer.data)
        return Response(serializer.errors)

        
# View for get all quiz


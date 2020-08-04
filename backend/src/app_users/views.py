from django.shortcuts import render
from rest_framework import generics

from .models import Users
from .serializers import UserSerializer

class ListUser(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer

class DetailUser(generics.RetrieveUpdateDestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
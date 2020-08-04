from django.shortcuts import render
from rest_framework import generics

from .models import TestReturn
from .serializers import TestReturnSerializer

# Create your views here.

class ListTestReturn(generics.ListCreateAPIView):
    queryset = TestReturn.objects.all()
    serializer_class = TestReturnSerializer

class DetailTestReturn(generics.RetrieveUpdateDestroyAPIView):
    queryset = TestReturn.objects.all()
    serializer_class = TestReturnSerializer
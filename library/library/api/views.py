from django.db.models import query
from django.shortcuts import render

from rest_framework import generics, permissions

from .serializers import *
from library.library.models import *

# Create your views here.

class TestView(generics.ListAPIView):
    serializer_class = TestSerializer
    queryset = Book.objects.all()
    permission_classes = [permissions.AllowAny]

class AuthorView(generics.ListCreateAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    permission_classes = [permissions.AllowAny]
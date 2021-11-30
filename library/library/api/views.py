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
    queryset = Author.objects.all
    permission_classes = [permissions.AllowAny]

class DeweyDecimalView(generics.ListCreateAPIView, generics.UpdateAPIView):
    serializer_class = DeweyDecimalSerializer
    queryset = DeweyDecimal.objects.all()
    permission_classes = [permissions.AllowAny]

class StudentView(generics.ListCreateAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    permission_classes = [permissions.AllowAny]

class TeacherView(generics.ListCreateAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()
    permission_classes = [permissions.AllowAny]

class BookView(generics.ListCreateAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = [permissions.AllowAny]

class CheckoutView(generics.ListCreateAPIView, generics.DestroyAPIView):
    serializer_class = CheckoutSerializer
    queryset = Checkout.objects.all()
    permission_classes = [permissions.AllowAny]
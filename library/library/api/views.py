from django.db.models import query
from django.shortcuts import render

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_framework import generics, permissions

from .serializers import *
from library.library.models import *

# Create your views here.


class TestView(generics.ListAPIView):
    serializer_class = TestSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        queryset = Book.objects.all()
        title = self.request.query_params.get('title')
        if title is not None:
            queryset = queryset.filter(title__iexact=title)
        return queryset


class AuthorView(generics.ListCreateAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all
    permission_classes = [permissions.IsAuthenticated]


class StudentView(generics.ListCreateAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Student.objects.all()
        first_name = self.request.query_params.get('first_name')
        last_name = self.request.query_params.get('last_name')
        idnum = self.request.query_params.get('id')
        email = self.request.query_params.get('email')
        if first_name is not None:
            queryset = queryset.filter(first_name__icontains=first_name)
        if last_name is not None:
            queryset = queryset.filter(last_name__icontains=last_name)
        if idnum is not None:
            queryset = queryset.filter(id__iexact=idnum)
        if email is not None:
            queryset = queryset.filter(email__icontains=email)
        return queryset


class TeacherView(generics.ListCreateAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    serializer_class = TeacherSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Teacher.objects.all()
        first_name = self.request.query_params.get('first_name')
        last_name = self.request.query_params.get('last_name')
        email = self.request.query_params.get('email')
        room_number = self.request.query_params.get('room_number')
        if first_name is not None:
            queryset = queryset.filter(first_name__icontains=first_name)
        if last_name is not None:
            queryset = queryset.filter(last_name__icontains=last_name)
        if email is not None:
            queryset = queryset.filter(email__icontains=email)
        if room_number is not None:
            queryset = queryset.filter(room_number__iexact=room_number)
        return queryset


class BookView(generics.ListCreateAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Book.objects.all()
        title = self.request.query_params.get('title')
        author = self.request.query_params.get('author')
        barcode = self.request.query_params.get('barcode')
        call_number = self.request.query_params.get('call_number')
        if title is not None:
            queryset = queryset.filter(title__icontains=title)
        if author is not None:
            queryset = queryset.filter(author__id=int(author))
        if barcode is not None:
            queryset = queryset.filter(barcode__iexact=barcode)
        if call_number is not None:
            queryset = queryset.filter(call_number__id=int(call_number))
        return queryset


class CheckoutView(generics.ListCreateAPIView, generics.DestroyAPIView):
    serializer_class = CheckoutSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Checkout.objects.all()
        book = self.request.query_params.get('book')
        student = self.request.query_params.get('student')
        if book is not None:
            queryset = queryset.filter(book__title__icontains=book)
        if student is not None:
            queryset = queryset.filter(student__id=int(student))
        return queryset

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)
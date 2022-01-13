from django.db.models import query
from django.shortcuts import render

from rest_framework import generics, permissions, status
from rest_framework.response import Response

from .serializers import *
from library.library.models import *


from django.core.mail import send_mail
from library.library.forms import EmailForm
from library.library.tasks import send_overdue_email
from django.conf import settings
from django.shortcuts import render


# Create your views here.


class TestView(generics.ListAPIView):
    serializer_class = TestSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        queryset = Book.objects.all()
        title = self.request.query_params.get('title')
        if title is not None:
            queryset = queryset.filter(title__iexact=title)
        return queryset


class AuthorView(generics.ListCreateAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all
    permission_classes = [permissions.AllowAny]


class StudentView(generics.ListCreateAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    serializer_class = StudentSerializer
    permission_classes = [permissions.AllowAny]

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
    permission_classes = [permissions.AllowAny]

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
    permission_classes = [permissions.AllowAny]

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
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        queryset = Checkout.objects.all()
        book = self.request.query_params.get('book')
        student = self.request.query_params.get('student')
        if book is not None:
            queryset = queryset.filter(book__title__icontains=book)
        if student is not None:
            queryset = queryset.filter(student__id=int(student))
        return queryset

    def perform_create(self, serializer):
        checkout = serializer.save()
        send_overdue_email(checkout)

        # wait the seconds until due date
        # wait((checkout.due_date - checkout.checkout_time).total_seconds())

        # # try to get checkout object from db if exists
        # try:
        #     checkout = Checkout.objects.get(id=checkout.id)
        # #     recipient = checkout.student.email #recipient = student email 
        # #     send_mail('A cool subject', 'A stunning message', settings.EMAIL_HOST_USER, [recipient], fail_silently=False)
            
        # except:
        #     result.abort()
        #     # the book was checked in
        #     pass

            


from django.shortcuts import render
from .models import  Student
from .serializers import StudentSerializer
from rest_framework import viewsets

class StudentView (viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
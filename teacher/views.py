from django.shortcuts import render
from .models import  Teacher
from .serializers import TeacherSerializer
from rest_framework import viewsets

class TeacherView (viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
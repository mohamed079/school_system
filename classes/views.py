from django.shortcuts import render
from .models import  Classes
from .serializers import ClassesSerializer
from rest_framework import viewsets

class ClassesView (viewsets.ModelViewSet):
    queryset = Classes.objects.all()
    serializer_class = ClassesSerializer
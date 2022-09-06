from django.shortcuts import render
from .models import  Clothes
from .serializers import ClothesSerializer
from rest_framework import viewsets

class ClothesView (viewsets.ModelViewSet):
    queryset = Clothes.objects.all()
    serializer_class = ClothesSerializer
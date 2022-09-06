from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Clothes

class ClothesSerializer (serializers.ModelSerializer):
    class Meta : 
        model = Clothes
        fields = "__all__"
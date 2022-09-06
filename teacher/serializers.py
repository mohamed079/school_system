from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Teacher

class TeacherSerializer (serializers.ModelSerializer):
    class Meta : 
        model = Teacher
        fields = "__all__"
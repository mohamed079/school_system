from email.mime import image
from pydoc import describe
from unicodedata import name
from venv import create
from django.db import models

class Teacher (models.Model):
    class SubjectName (models.Choices):
        Arabic = "Arabic"
        English = "English"
        Maths = "Maths"
        Social_Studies = "Social Studies"
        Sciences = "Sciences"
        Art_Education = "Art Education"
        Religious_Education = "Religious Education" 
        Music_Education = "Music Education"
        Information_Technology = "Information Technology"

    name = models.CharField(max_length=100)
    age = models.DecimalField(max_digits=2 , decimal_places=0)
    subject = models.CharField(choices=SubjectName.choices , default=SubjectName.Arabic, max_length=50 )
    describtion = models.TextField(default='' , null=True , blank=True)
    image = models.ImageField(upload_to = "photo%y%m%d")
    salary = models.DecimalField(max_digits=5 , decimal_places=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

    def __str__(self):
      return self.name

from django.db import models
from classes.models import Classes
class Student (models.Model):
    class Gender (models.Choices):
        male = "Male"
        female = "Female"
    class SchoolYear(models.Choices):
        First_grade = "First grade"
        Second_grade = "Second grade"
        third_grade = "third grade"
        fourth_grade = "fourth grade"
        fifth_grade = "fifth grade"
        Sixth_grade = "Sixth grade"      
    name = models.CharField(max_length=100)
    gender = models.CharField(choices=Gender.choices , default=Gender.male , max_length=7)
    date_of_birth= models.DateField(max_length=8)
    phone = models.CharField(max_length=12)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    student_class = models.ForeignKey(Classes , related_name="student" , on_delete=models.CASCADE)
    school_year = models.CharField(choices=SchoolYear.choices , default=SchoolYear.First_grade , max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
    
    def __str__(self):
      return self.name

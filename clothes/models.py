from django.db import models

class Clothes(models.Model):
      class Type (models.Choices):
          trouser = "trouser"
          T_shirt = "T-shirt"

      type = models.CharField(choices=Type.choices , default=Type.T_shirt , max_length=10)
      price = models.DecimalField(max_digits=3 , decimal_places=1)

      def __str__(self):
           return self.type

      
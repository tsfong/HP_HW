from django.db import models
from ...houses.models.house import House 


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    family_name = models.CharField(max_length=100)
    house = models.ForeignKey(House, related_name='house', null=True)


    def __str__(self):
        return self.name

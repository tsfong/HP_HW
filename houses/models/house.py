from django.db import models
from ...schools.models.school import School 

# Create your models here.
class House(models.Model):
    name = models.CharField(max_length=100)
    animal = models.CharField(max_length=100)
    slogan = models.CharField(max_length=100)
    school = models.ForeignKey(School, related_name='house', null=True)

    def __str__(self):
        return self.name

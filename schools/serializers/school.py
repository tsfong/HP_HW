from rest_framework import serializers
from ..models.school import School


class SchoolSerializer(serializers.ModelSerializer):
     # Define meta class
    class Meta:
         # Specify the model from which to define the fields
        model = School
        # Define fields to be returned
        fields = '__all__'

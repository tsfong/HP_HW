from rest_framework import serializers
from ..models.house import House

class HouseSerializer(serializers.ModelSerializer):
     # Define meta class
    class Meta:
         # Specify the model from which to define the fields
        model = House
        # Define fields to be returned
        fields = ('name', 'animal', 'slogan', 'school')

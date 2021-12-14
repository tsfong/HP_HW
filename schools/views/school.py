from rest_framework.views import APIView
from rest_framework.response import Response
from ..serializers.school import SchoolSerializer
from ..models.school import School
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.views import View
import json

# /schools
class SchoolsView(APIView):
    # POST /schools
    def post(self, request):
        school = SchoolSerializer(data=request.data)
        if school.is_valid():
             school.save()
             return Response(school.data, status=status.HTTP_201_CREATED)
        else:
            return Response(school.errors, status=status.HTTP_400_BAD_REQUEST)

    # GET /schools
    def get(self, request):
        schools = School.objects.all()
        data = SchoolSerializer(schools, many=True).data
        return Response(data)

# /schools/:id
class SchoolView(APIView):
    def patch(self, request, pk):
        school = get_object_or_404(School, pk=pk)
        updated_school = SchoolSerializer(school, data=request.data, partial=True)
        if updated_school.is_valid():
            updated_school.save()
            return Response(updated_school.data)

    def put(self, request, pk):
        school = get_object_or_404(School, pk=pk)
        updated_school = SchoolSerializer(school, data=request.data, partial=True)
        if updated_school.is_valid():
            updated_school.save()
            return Response(updated_school.data)

    def delete(self, request, pk):
        school = get_object_or_404(School, pk=pk)
        school.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # GET /schools/:id
    def get(self, request, pk):
        school = get_object_or_404(School, pk=pk)
        data = SchoolSerializer(school).data
        return Response(data)

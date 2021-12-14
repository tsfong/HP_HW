from rest_framework.views import APIView
from rest_framework.response import Response
from ..serializers.student import StudentSerializer
from ..models.student import Student
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.views import View
import json

# /students
class StudentsView(APIView):
    # POST /students
    def post(self, request):
        student = StudentSerializer(data=request.data)
        if student.is_valid():
             student.save()
             return Response(student.data, status=status.HTTP_201_CREATED)
        else:
            return Response(student.errors, status=status.HTTP_400_BAD_REQUEST)

    # GET /students
    def get(self, request):
        students = Student.objects.all()
        data = StudentSerializer(students, many=True).data
        return Response(data)

# /student/:id
class StudentView(APIView):
    def patch(self, request, pk):
        student = get_object_or_404(Student, pk=pk)
        updated_student = StudentSerializer(student, data=request.data, partial=True)
        if updated_student.is_valid():
            updated_student.save()
            return Response(updated_student.data)

    def put(self, request, pk):
        student = get_object_or_404(Student, pk=pk)
        updated_student = StudentSerializer(student, data=request.data, partial=True)
        if updated_student.is_valid():
            updated_student.save()
            return Response(updated_student.data)

    def delete(self, request, pk):
        student = get_object_or_404(Student, pk=pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # GET /students/:id
    def get(self, request, pk):
        student = get_object_or_404(Student, pk=pk)
        data = StudentSerializer(student).data
        return Response(data)

# house/urls.py
from django.urls import path
from .views import student

urlpatterns = [
    # path('', views.index, name='index'),
    path('students/', student.StudentsView.as_view(), name='index'),
    # path('<int:pk>/', views.show, name='Student-detail'),
    path('students/<int:pk>/', student.StudentView.as_view(), name='Student-detail'),
]
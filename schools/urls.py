# schools/urls.py
from django.urls import path
from .views import school

urlpatterns = [
    # path('', views.index, name='index'),
    path('schools/', school.SchoolsView.as_view(), name='index'),
    # path('<int:pk>/', views.show, name='School-detail'),
    path('schools/<int:pk>/', school.SchoolView.as_view(), name='School-detail'),
]
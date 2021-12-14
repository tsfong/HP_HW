# house/urls.py
from django.urls import path
from .views import house

urlpatterns = [
    # path('', views.index, name='index'),
    path('dorms/', house.HousesView.as_view(), name='index'),
    # path('<int:pk>/', views.show, name='House-detail'),
    path('dorms/<int:pk>/', house.HouseView.as_view(), name='House-detail'),
]
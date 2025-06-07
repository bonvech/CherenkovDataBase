from django.urls import path
from . import views

urlpatterns = [
    path('histogram/', views.histogram, name='histogram'),
]

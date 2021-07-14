from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('comoestas/', views.comoestas),
    path('mm/', views.bien)
]

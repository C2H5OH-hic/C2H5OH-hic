from django.urls import path
from . import views

urlpatterns = [
    path('holaa/', views.holaa),
    path('comoestas/', views.comoestas)
]

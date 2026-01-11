from django.urls import path
from . import views

urlpatterns = [
    path('create/',views.create_autor, name='create_autor'),
]
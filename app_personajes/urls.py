from django.urls import path
from . import views

urlpatterns = [
    path('galeria/',views.personajes),
    path('create/',views.create),
    path('delete/',views.delete)
]
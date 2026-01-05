from django.urls import path
from . import views

urlpatterns = [
    path('test/',views.tester,name='test_app'),
    path('create/',views.create),
    path('delete/',views.delete)
]
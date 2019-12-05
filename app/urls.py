from django.urls import path
from . import views

urlpatterns = [
    path('', views.auth_check, name='auth_check'),
]

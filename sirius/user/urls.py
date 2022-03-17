from django.contrib import admin
from .views import *
from django.urls import path

app_name = 'user'

urlpatterns = [
    path('sign-up/', sign_up, name='sign_up'),
    path('sign-in/', sign_in, name='sign_in'),
    path('sign-out/', sign_out, name='sign_out'),
    path('dashboard/<pk>/', dashboard, name='dashboard'),
]
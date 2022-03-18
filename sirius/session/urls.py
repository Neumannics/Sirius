from django.urls import path
from .views import *

app_name = 'session'

urlpatterns = [
    path('create/', create_session, name='create_session'),
]
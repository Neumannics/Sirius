from django.urls import path
from .views import *

app_name = 'authorization'

urlpatterns = [
    path('create_role/', create_role, name='create_role'),
    path('<pk>/', show_roles, name='show_roles'),
    path('update_role/<pk>/', update_role, name='update_role'),
]
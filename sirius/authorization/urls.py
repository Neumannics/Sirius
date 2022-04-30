from django.urls import path
from .views import *

app_name = 'authorization'

urlpatterns = [
    path('create-role/', create_role, name='create_role'),
    path('roles/', show_roles, name='show_roles'),
    path('update-roles/', update_roles, name='update_roles'),
    path('permissions/', show_permissions, name='show_permissions'),
    path('update-permissions/', update_permissions, name='update_permissions'),
]
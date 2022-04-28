from django.urls import path
from .views import *

app_name = 'authorization'

urlpatterns = [
    path('create-role/', create_role, name='create_role'),
    path('memberships/', show_roles, name='show_roles'),
    path('update-membership/<user_pk>', update_membership, name='update_membership'),
]
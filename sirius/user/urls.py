from django.contrib import admin
from django.urls import path

from . import views

app_name = 'user'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('<u_pk>/dashboard/', views.dashboard, name='dashboard'),
    # path('<u_pk>/settings/', views.settings, name='settings'),
]
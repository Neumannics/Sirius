from django.contrib import admin
from django.urls import path
from django.urls.conf import include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.landing, name='landing_path'),
    path("__reload__/", include("django_browser_reload.urls")),
    path('auth/', include('user.urls')),
    path('team/', include('team.urls')),
    path('session/', include('session.urls')),
    path('authorization/', include('authorization.urls'))
]
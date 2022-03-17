from django.contrib import admin
from .models import Roles, Permissions

# Register your models here.
admin.site.register(Roles)
admin.site.register(Permissions)
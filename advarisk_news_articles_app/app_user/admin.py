from django.contrib import admin

# Register your models here.
from app_user.models import AppUsers
admin.site.register(AppUsers)
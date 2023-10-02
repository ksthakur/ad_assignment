from django.db import models


class AppUsers(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
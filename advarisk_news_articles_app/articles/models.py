from django.db import models
from app_user.models import AppUsers

class ArticleUsers(models.Model):
    search_data = models.CharField(max_length=200)
    search_user_id = models.ForeignKey(AppUsers, on_delete=models.CASCADE)

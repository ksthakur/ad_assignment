from articles.models import ArticleUsers
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

class ArticleSerializer(serializers.ModelSerializer):

	class Meta:
		model = ArticleUsers
		fields = ['search_data', 'search_user_id']
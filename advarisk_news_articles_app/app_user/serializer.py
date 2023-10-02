from app_user.models import AppUsers
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

class AppUserSerializer(serializers.ModelSerializer):

	class Meta:
		model = AppUsers
		fields = ['name', 'email']
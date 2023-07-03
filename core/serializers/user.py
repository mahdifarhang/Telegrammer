from rest_framework import serializers

from core.models import User

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = [
			'id',
			'first_name',
			'last_name',
			'username',
			'email',
			'is_staff',
			'is_superuser',
			'date_joined',
			'last_login',
			'is_active',
		]
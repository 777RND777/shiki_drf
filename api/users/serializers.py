from rest_framework.serializers import ModelSerializer

from .models import User


class RegistrationSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "password"]
        extra_kwargs = {
            'username': {'required': True},
            'password': {'required': True, 'write_only': True}
        }


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "password"]

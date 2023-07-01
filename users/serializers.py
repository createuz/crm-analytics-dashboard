from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password2')
        extra_kwargs = {
            'password2': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password2')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
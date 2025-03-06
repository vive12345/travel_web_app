# This serializer is used to convert Django's User model into JSON format for API responses and handle user registration.
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}# Hide password in responses

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data) # Ensures password hashing
        return user
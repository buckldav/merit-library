from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "name", "url"]

        extra_kwargs = {
            "url": {"view_name": "api:user-detail", "lookup_field": "username"}
        }


# Testing Serializer
class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'title',
            'description',
            'owner'
        )
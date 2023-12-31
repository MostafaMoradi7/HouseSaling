from rest_framework.serializers import ModelSerializer
from .models import MessageModel
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "password",
        )

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation.pop("password", None)
        return representation

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class MessageSerializer(ModelSerializer):
    class Meta:
        model = MessageModel
        fields = ("message",)

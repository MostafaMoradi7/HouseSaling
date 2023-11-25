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

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    def to_representation(self, instance):
        if (
            self.context.get("request")
            and self.context["request"].method == "GET"
        ):
            data = super().to_representation(instance)
            data.pop("password", None)
            return data
        return super().to_representation(instance)


class MessageSerializer(ModelSerializer):
    class Meta:
        model = MessageModel
        fields = ("message",)

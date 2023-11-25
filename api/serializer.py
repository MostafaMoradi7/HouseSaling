from rest_framework.serializers import ModelSerializer, ValidationError
from .models import HouseModel
from users.serializers import UserSerializer
from django.contrib.auth import get_user_model


class HouseSerializer(ModelSerializer):
    class Meta:
        model = HouseModel
        fields = (
            "area",
            "floor",
            "city",
            "price",
            "status",
            "seller",
            "buyer",
        )

    seller = UserSerializer(read_only=True)
    buyer = UserSerializer(read_only=True)

    def get_fields(self, *args, **kwargs):
        fields = super().get_fields(*args, **kwargs)

        if self.context.get("request").method != "POST":
            fields["seller"].read_only = True

        if self.context.get("request").method == "PATCH":
            fields["buyer"].read_only = True
            fields["status"].read_only = True
            fields["area"].read_only = True
            fields["floor"].read_only = True
            fields["city"].read_only = True
            fields["price"].read_only = True
            fields["seller"].read_only = True

        return fields

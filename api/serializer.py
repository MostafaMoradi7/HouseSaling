from rest_framework.serializers import ModelSerializer
from .models import HouseModel
from users.serializers import UserSerializer


class HouseSerializer(ModelSerializer):
    class Meta:
        model = HouseModel
        fields = (
            "unique_id",
            "area",
            "floor",
            "city",
            "price",
            "status",
            "seller",
            "buyer",
        )
        extra_kwargs = {
            "unique_id": {"read_only": True},
        }

    seller = UserSerializer(read_only=True)
    buyer = UserSerializer(read_only=True)

    def create(self, validated_data):
        validated_data["seller"] = self.context["request"].user
        validated_data["status"] = "FREE"
        return super().create(validated_data)

    def get_fields(self, *args, **kwargs):
        fields = super().get_fields(*args, **kwargs)

        if self.context.get("request").method != "POST":
            fields["seller"].read_only = True
            fields["status"].read_only = True

        if self.context.get("request").method == "PATCH":
            fields["buyer"].read_only = True
            fields["status"].read_only = True
            fields["area"].read_only = True
            fields["floor"].read_only = True
            fields["city"].read_only = True
            fields["price"].read_only = True
            fields["seller"].read_only = True

        return fields

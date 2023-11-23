from rest_framework.serializers import ModelSerializer
from .models import HouseModel


class HouseSerializer(ModelSerializer):
    class Meta:
        model = HouseModel
        fields = ("area", "floor", "city", "price", "status")

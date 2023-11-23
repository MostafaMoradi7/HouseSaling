from rest_framework.viewsets import ModelViewSet
from .serializer import HouseSerializer
from .models import HouseModel


# Create your views here.
class HouseViewSet(ModelViewSet):
    queryset = HouseModel.objects.all()
    serializer_class = HouseSerializer

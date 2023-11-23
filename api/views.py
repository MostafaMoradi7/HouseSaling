from rest_framework.viewsets import ModelViewSet
from .serializer import HouseSerializer
from .models import HouseModel
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class HouseViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = HouseModel.objects.all()
    serializer_class = HouseSerializer

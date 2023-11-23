from rest_framework.viewsets import ModelViewSet
from .serializer import HouseSerializer
from .models import HouseModel
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend


class HousePagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = "page_size"
    max_page_size = 1000


class HouseViewSet(ModelViewSet):
    queryset = HouseModel.objects.all()
    permission_classes = (IsAuthenticated,)
    pagination_class = HousePagination
    serializer_class = HouseSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ("area", "floor", "city", "price", "status")

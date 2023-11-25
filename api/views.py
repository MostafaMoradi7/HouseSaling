from rest_framework.viewsets import ModelViewSet
from .serializer import HouseSerializer
from .models import HouseModel
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.serializers import ValidationError
from rest_framework.response import Response
from rest_framework import status


class HousePagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = "page_size"
    max_page_size = 1000


class HouseViewSet(ModelViewSet):
    queryset = HouseModel.objects.all().order_by("price")
    permission_classes = (IsAuthenticated,)
    pagination_class = HousePagination
    serializer_class = HouseSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ("area", "floor", "city", "price", "status")

    def create(self, request, *args, **kwargs):
        data = request.data
        user = request.user

        data["seller"] = user.id
        data["buyer"] = None
        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            raise ValidationError(f"Not Valid {serializer.errors}")

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.seller != request.user:
            return Response(
                {"error": "You do not have permission to update this object."},
                status=status.HTTP_403_FORBIDDEN,
            )
        data = request.data
        data["buyer"] = None
        data["seller"] = request.user.id
        serializer = self.get_serializer(instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()

        if instance.seller == request.user:
            return Response(
                {"error": "You CAN'T buy your own house!"},
                status=status.HTTP_403_FORBIDDEN,
            )
        serializer = self.get_serializer(
            instance, data=request.data, partial=True
        )
        if serializer.is_valid():
            instance.status = "BAUGHT"
            instance.buyer = request.user
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.seller != request.user:
            return Response(
                {
                    "forbidden": "You do not have permission to delete this object."
                },
                status=status.HTTP_403_FORBIDDEN,
            )
        if instance.buyer:
            return Response(
                {
                    "forbidden": "This House does not belong to you anymore! so you can not delete it!"
                },
                status=status.HTTP_403_FORBIDDEN,
            )
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

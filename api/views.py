from rest_framework.viewsets import ModelViewSet
from .serializer import HouseSerializer
from .models import HouseModel
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import PermissionDenied, ValidationError
from django.core.exceptions import ObjectDoesNotExist


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
        try:
            data = request.data
            user = request.user

            data["seller"] = user.id
            data["buyer"] = None
            serializer = self.get_serializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data)
            else:
                raise ValidationError(serializer.errors)
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_400_BAD_REQUEST
            )

    def update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            if instance.seller != request.user:
                raise PermissionDenied(
                    "You do not have permission to update this object."
                )

            data = request.data
            data["buyer"] = None
            data["seller"] = request.user.id
            serializer = self.get_serializer(instance, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                raise ValidationError(serializer.errors)
        except PermissionDenied as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_403_FORBIDDEN
            )
        except ObjectDoesNotExist as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_404_NOT_FOUND
            )

    def partial_update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()

            if instance.seller == request.user:
                raise PermissionDenied("You CAN'T buy your own house!")

            if instance.buyer is not None:
                raise PermissionDenied("House have been sold out!")

            serializer = self.get_serializer(
                instance, data=request.data, partial=True
            )
            if serializer.is_valid():
                instance.status = "BAUGHT"
                instance.buyer = request.user
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                raise ValidationError(serializer.errors)
        except PermissionDenied as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_403_FORBIDDEN
            )
        except ObjectDoesNotExist as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_404_NOT_FOUND
            )

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            if instance.seller != request.user:
                raise PermissionDenied(
                    "You do not have permission to delete this object."
                )
            if instance.buyer:
                raise PermissionDenied(
                    "This House does not belong to you anymore! so you can not delete it!"
                )
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except PermissionDenied as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_403_FORBIDDEN
            )
        except ObjectDoesNotExist as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_404_NOT_FOUND
            )

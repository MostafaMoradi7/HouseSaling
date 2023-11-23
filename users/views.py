from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer, MessageSerializer
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny


class UserRegistrationView(APIView):
    permission_classes = (AllowAny,)

    @extend_schema(
        request=UserSerializer,
        responses={
            status.HTTP_201_CREATED: UserSerializer,
            status.HTTP_400_BAD_REQUEST: MessageSerializer,
        },
    )
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "username": serializer.data["username"],
                "status": "registered successfully",
            }
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

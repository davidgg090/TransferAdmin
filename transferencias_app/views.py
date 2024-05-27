from rest_framework import generics, permissions
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from django.contrib.auth.models import User
from .models import Transferencia
from .serializers import TransferenciaSerializer, UserSerializer
from .services import TransferenciaService


class TransferenciaListCreate(generics.ListCreateAPIView):
    """
    A view for listing and creating transferencia objects.

    Explanation:
    Uses a serializer to handle the data and a service to create a new transferencia instance.
    """

    queryset = Transferencia.objects.all()
    serializer_class = TransferenciaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        service = TransferenciaService()
        service.create_transferencia(**serializer.validated_data)


class TransferenciaRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """
    A view for retrieving, updating, and deleting a specific transferencia object.

    Explanation:
    Uses a serializer to handle the data and a service to update or delete the transferencia instance.
    """

    queryset = Transferencia.objects.all()
    serializer_class = TransferenciaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        service = TransferenciaService()
        service.update_transferencia(transferencia=self.get_object(), **serializer.validated_data)

    def perform_destroy(self, instance):
        service = TransferenciaService()
        service.delete_transferencia(instance)


class UserCreate(generics.CreateAPIView):
    """
    A view for creating a new user.

    Explanation:
    Uses a serializer to handle the data and allows any user to access this endpoint.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class TokenObtainPair(TokenObtainPairView):
    """
    A view for obtaining a new access and refresh token pair.

    Explanation:
    Uses a serializer to handle the data and obtain a new access and refresh token pair.
    """

    serializer_class = TokenObtainPairSerializer

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from rest_framework import generics, permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response

from .models import Transferencia, Cliente, Beneficiario
from .permissions import IsTokenAuthenticated
from .serializers import TransferenciaSerializer, UserSerializer, ClienteSerializer, BeneficiarioSerializer
from .services import TransferenciaService, ClienteService, BeneficiarioService


class ClienteListCreate(generics.ListCreateAPIView):
    """
    A view for listing and creating Cliente objects.

    Explanation:
    Uses a serializer to handle the data and a service to create a new Cliente instance.
    """

    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [IsTokenAuthenticated]
    authentication_classes = [JWTAuthentication]

    def perform_create(self, serializer):
        ClienteService.create_cliente(**serializer.validated_data)


class ClienteRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """
    A view for retrieving, updating, and deleting a specific Cliente object.

    Explanation:
    Uses a serializer to handle the data and a service to update or delete the Cliente instance.
    """

    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [IsTokenAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_object(self):
        obj = get_object_or_404(Cliente, id=self.kwargs['pk'])
        return obj

    def perform_update(self, serializer):
        cliente = self.get_object()
        service = ClienteService()
        updated_cliente = service.update_cliente(cliente=cliente, **serializer.validated_data)
        return Response(self.get_serializer(updated_cliente).data)

    def perform_destroy(self, instance):
        cliente = self.get_object()
        service = ClienteService()
        service.delete_cliente(cliente)


class BeneficiarioListCreate(generics.ListCreateAPIView):
    """
    A view for listing and creating Beneficiario objects.

    Explanation:
    Uses a serializer to handle the data and a service to create a new Beneficiario instance.
    """

    queryset = Beneficiario.objects.all()
    serializer_class = BeneficiarioSerializer
    permission_classes = [IsTokenAuthenticated]
    authentication_classes = [JWTAuthentication]

    def perform_create(self, serializer):
        BeneficiarioService.create_beneficiario(**serializer.validated_data)


class BeneficiarioRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """
    A view for retrieving, updating, and deleting a specific Beneficiario object.

    Explanation:
    Uses a serializer to handle the data and a service to update or delete the Beneficiario instance.
    """

    queryset = Beneficiario.objects.all()
    serializer_class = BeneficiarioSerializer
    permission_classes = [IsTokenAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_object(self):
        obj = get_object_or_404(Beneficiario, id=self.kwargs['pk'])
        return obj

    def perform_update(self, serializer):
        beneficiario = self.get_object()
        service = BeneficiarioService()
        updated_beneficiario = service.update_beneficiario(beneficiario=beneficiario, **serializer.validated_data)
        return Response(self.get_serializer(updated_beneficiario).data)

    def perform_destroy(self, instance):
        beneficiario = self.get_object()
        service = BeneficiarioService()
        service.delete_beneficiario(beneficiario)


class TransferenciaListCreate(generics.ListCreateAPIView):
    """
    A view for listing and creating transferencia objects.

    Explanation:
    Uses a serializer to handle the data and a service to create a new transferencia instance.
    """

    queryset = Transferencia.objects.all()
    serializer_class = TransferenciaSerializer
    permission_classes = [IsTokenAuthenticated]
    authentication_classes = [JWTAuthentication]

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
    permission_classes = [IsTokenAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_object(self):
        obj = get_object_or_404(Transferencia, id=self.kwargs['pk'])
        return obj

    def perform_update(self, serializer):
        transferencia = self.get_object()
        service = TransferenciaService()
        updated_transferencia = service.update_transferencia(transferencia=transferencia, **serializer.validated_data)
        return Response(self.get_serializer(updated_transferencia).data)

    def perform_destroy(self, instance):
        transferencia = self.get_object()
        service = TransferenciaService()
        service.delete_transferencia(transferencia)


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

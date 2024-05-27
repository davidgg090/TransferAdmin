from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Cliente, Beneficiario, Transferencia


class ClienteSerializer(serializers.ModelSerializer):
    """
    Serializer for the Cliente model.

    Explanation:
    Defines how the Cliente model should be serialized, including all fields.
    """

    class Meta:
        model = Cliente
        fields = '__all__'


class BeneficiarioSerializer(serializers.ModelSerializer):
    """
    Serializer for the Beneficiario model.

    Explanation:
    Defines how the Beneficiario model should be serialized, including all fields.
    """

    class Meta:
        model = Beneficiario
        fields = '__all__'


class ClienteSerializer(serializers.ModelSerializer):
    """
    Serializer for the Cliente model.

    Explanation:
    Defines how the Cliente model should be serialized, including all fields.
    """

    class Meta:
        model = Cliente
        fields = '__all__'


class BeneficiarioSerializer(serializers.ModelSerializer):
    """
    Serializer for the Beneficiario model.

    Explanation:
    Defines how the Beneficiario model should be serialized, including all fields.
    """

    class Meta:
        model = Beneficiario
        fields = '__all__'


class TransferenciaSerializer(serializers.ModelSerializer):
    """
    Serializer for the Transferencia model.

    Explanation:
    Defines how the Transferencia model should be serialized, including all fields.
    """

    class Meta:
        model = Transferencia
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User model.

    Explanation:
    Defines how the User model should be serialized, including specific fields. Provides a method to create a new user instance.

    Args:
    - validated_data (dict): The validated data for creating a new user.

    Returns:
    - User: The created user instance.
    """

    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data.get('email')
        )
        return user

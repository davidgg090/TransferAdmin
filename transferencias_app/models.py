from django.db import models
import uuid


class Cliente(models.Model):
    """
    A model representing a client.

    Explanation:
    This model represents a client with attributes for full name, address, and phone number.

    Args:
    - nombre_completo (str): The full name of the client.
    - direccion (str): The address of the client.
    - telefono (str): The phone number of the client.

    Returns:
    - str: The full name of the client.
    """

    nombre_completo = models.CharField(max_length=255)
    direccion = models.TextField()
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre_completo


class Beneficiario(models.Model):
    """
    A model representing a beneficiary.

    Explanation:
    This model represents a beneficiary with attributes for full name, relationship, date of birth, and gender.

    Args:
    - nombre_completo (str): The full name of the beneficiary.
    - parentesco (str): The relationship of the beneficiary.
    - fecha_nacimiento (date): The date of birth of the beneficiary.
    - sexo (str): The gender of the beneficiary.

    Returns:
    - str: The full name of the beneficiary.
    """

    nombre_completo = models.CharField(max_length=255)
    parentesco = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    sexo = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre_completo


class Transferencia(models.Model):
    """
    A model representing a transfer.

    Explanation:
    This model represents a transfer with attributes for ID, client, beneficiary, amount, transfer date, and status.

    Args:
    - cliente (Cliente): The client initiating the transfer.
    - beneficiario (Beneficiario): The beneficiary of the transfer.
    - monto (Decimal): The amount of the transfer.
    - fecha_transferencia (date): The date of the transfer.
    - estado (str): The status of the transfer.

    Returns:
    - str: A string representation of the transfer.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    beneficiario = models.ForeignKey(Beneficiario, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_transferencia = models.DateField()
    estado = models.CharField(max_length=20, choices=[
        ('pendiente', 'Pendiente'),
        ('completada', 'Completada'),
        ('cancelada', 'Cancelada'),
    ])

    def __str__(self):
        return f'Transferencia {self.id}'

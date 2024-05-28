from .models import Transferencia, Cliente, Beneficiario
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.db import IntegrityError, transaction


class ClienteService:
    """
    A service class for managing Cliente objects.

    Explanation:
    Provides static methods for creating, updating, and deleting Cliente instances.

    Args:
    - nombre_completo (str): The full name of the client.
    - direccion (str): The address of the client.
    - telefono (str): The phone number of the client.

    Returns:
    - Cliente: The created, updated, or deleted Cliente instance.
    """

    @staticmethod
    def create_cliente(nombre_completo, direccion, telefono):
        try:
            with transaction.atomic():
                cliente = Cliente.objects.create(nombre_completo=nombre_completo, direccion=direccion, telefono=telefono)
            return cliente
        except IntegrityError as e:
            raise ValidationError(f"Error creating beneficiario: {e}") from e

    @staticmethod
    def update_cliente(cliente, **kwargs):
        try:
            with transaction.atomic():
                for field, value in kwargs.items():
                    if hasattr(cliente, field):
                        setattr(cliente, field, value)
                cliente.save()
            return cliente
        except IntegrityError as e:
            raise ValidationError(f"Error updating beneficiario: {e}") from e
        except ObjectDoesNotExist as e:
            raise ValidationError(f"Beneficiario does not exist: {e}") from e
        except Exception as e:
            raise ValidationError(f"Unexpected error: {e}") from e


    @staticmethod
    def delete_cliente(cliente):
        cliente.delete()


class BeneficiarioService:
    """
    A service class for managing Beneficiario objects.

    Explanation:
    Provides static methods for creating, updating, and deleting Beneficiario instances.

    Args:
    - nombre_completo (str): The full name of the beneficiary.
    - parentesco (str): The relationship of the beneficiary.
    - fecha_nacimiento (date): The date of birth of the beneficiary.
    - sexo (str): The gender of the beneficiary.

    Returns:
    - Beneficiario: The created, updated, or deleted Beneficiario instance.
    """

    @staticmethod
    def create_beneficiario(nombre_completo, parentesco, fecha_nacimiento, sexo):
        try:
            with transaction.atomic():
                beneficiario = Beneficiario.objects.create(nombre_completo=nombre_completo, parentesco=parentesco,
                                           fecha_nacimiento=fecha_nacimiento, sexo=sexo)
            return beneficiario
        except IntegrityError as e:
            raise ValidationError(f"Error creating beneficiario: {e}") from e
    @staticmethod
    def update_beneficiario(beneficiario, **kwargs):
        try:
            with transaction.atomic():
                for field, value in kwargs.items():
                    if hasattr(beneficiario, field):
                        setattr(beneficiario, field, value)
                beneficiario.save()
            return beneficiario
        except IntegrityError as e:
            raise ValidationError(f"Error updating beneficiario: {e}") from e
        except ObjectDoesNotExist as e:
            raise ValidationError(f"Beneficiario does not exist: {e}") from e
        except Exception as e:
            raise ValidationError(f"Unexpected error: {e}") from e

    @staticmethod
    def delete_beneficiario(beneficiario):
        beneficiario.delete()


class TransferenciaService:
    """
    A service class for managing transferencia objects.

    Provides methods for creating, updating, and deleting transferencia instances.

    Args:
    - cliente: The client for the transferencia.
    - beneficiario: The beneficiary for the transferencia.
    - monto: The amount of the transferencia.
    - fecha_transferencia: The date of the transferencia.
    - estado: The status of the transferencia.

    Returns:
    - Transferencia: The created, updated, or deleted transferencia instance.
    """

    def __init__(self, transferencia_model=Transferencia):
        self.transferencia_model = transferencia_model

    def create_transferencia(self, cliente_id, beneficiario_id, monto, fecha_transferencia, estado):
        try:
            cliente = Cliente.objects.get(id=cliente_id)
            beneficiario = Beneficiario.objects.get(id=beneficiario_id)
        except Cliente.DoesNotExist as e:
            raise ValidationError(f"Cliente with id {cliente_id} does not exist.") from e
        except Beneficiario.DoesNotExist as e:
            raise ValidationError(
                f"Beneficiario with id {beneficiario_id} does not exist."
            ) from e

        try:
            with transaction.atomic():
                transferencia = self.transferencia_model.objects.create(
                    cliente=cliente,
                    beneficiario=beneficiario,
                    monto=monto,
                    fecha_transferencia=fecha_transferencia,
                    estado=estado
                )
            return transferencia
        except IntegrityError as e:
            raise ValidationError(f"Error creating transferencia: {e}") from e

    def update_transferencia(self, transferencia, **kwargs):
        try:
            if 'cliente_id' in kwargs:
                kwargs['cliente'] = Cliente.objects.get(id=kwargs.pop('cliente_id'))
            if 'beneficiario_id' in kwargs:
                kwargs['beneficiario'] = Beneficiario.objects.get(id=kwargs.pop('beneficiario_id'))
        except Cliente.DoesNotExist as e:
            raise ValidationError(
                f"Cliente with id {kwargs.get('cliente_id')} does not exist."
            ) from e
        except Beneficiario.DoesNotExist as e:
            raise ValidationError(
                f"Beneficiario with id {kwargs.get('beneficiario_id')} does not exist."
            ) from e

        try:
            with transaction.atomic():
                for field, value in kwargs.items():
                    if hasattr(transferencia, field):
                        setattr(transferencia, field, value)
                transferencia.save()
            return transferencia
        except IntegrityError as e:
            raise ValidationError(f"Error updating transferencia: {e}") from e
        except ObjectDoesNotExist as e:
            raise ValidationError(f"Transferencia does not exist: {e}") from e
        except Exception as e:
            raise ValidationError(f"Unexpected error: {e}") from e

    def delete_transferencia(self, transferencia):
        try:
            with transaction.atomic():
                transferencia.estado = 'cancelada'
                transferencia.save()
            return transferencia
        except IntegrityError as e:
            raise ValidationError(f"Error deleting transferencia: {e}") from e
        except ObjectDoesNotExist as e:
            raise ValidationError(f"Transferencia does not exist: {e}") from e
        except Exception as e:
            raise ValidationError(f"Unexpected error: {e}") from e
from .models import Transferencia, Cliente, Beneficiario


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
        return Cliente.objects.create(nombre_completo=nombre_completo, direccion=direccion, telefono=telefono)

    @staticmethod
    def update_cliente(cliente, nombre_completo, direccion, telefono):
        cliente.nombre_completo = nombre_completo
        cliente.direccion = direccion
        cliente.telefono = telefono
        cliente.save()
        return cliente

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
        return Beneficiario.objects.create(nombre_completo=nombre_completo, parentesco=parentesco,
                                           fecha_nacimiento=fecha_nacimiento, sexo=sexo)

    @staticmethod
    def update_beneficiario(beneficiario, nombre_completo, parentesco, fecha_nacimiento, sexo):
        beneficiario.nombre_completo = nombre_completo
        beneficiario.parentesco = parentesco
        beneficiario.fecha_nacimiento = fecha_nacimiento
        beneficiario.sexo = sexo
        beneficiario.save()
        return beneficiario

    @staticmethod
    def delete_beneficiario(beneficiario):
        beneficiario.delete()


class TransferenciaService:
    """
    A service class for managing transferencia objects.

    Explanation:
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

    def create_transferencia(self, cliente, beneficiario, monto, fecha_transferencia, estado):
        transferencia = self.transferencia_model.objects.create(
            cliente=cliente,
            beneficiario=beneficiario,
            monto=monto,
            fecha_transferencia=fecha_transferencia,
            estado=estado
        )
        return transferencia

    def update_transferencia(self, transferencia, cliente, beneficiario, monto, fecha_transferencia, estado):
        transferencia.cliente = cliente
        transferencia.beneficiario = beneficiario
        transferencia.monto = monto
        transferencia.fecha_transferencia = fecha_transferencia
        transferencia.estado = estado
        transferencia.save()
        return transferencia

    def delete_transferencia(self, transferencia):
        transferencia.estado = 'cancelada'
        transferencia.save()
        return transferencia

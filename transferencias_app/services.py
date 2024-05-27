from .models import Transferencia


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

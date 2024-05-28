from django.test import TestCase
from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from ..services import TransferenciaService
from ..models import Transferencia, Cliente, Beneficiario


class TestTransferenciaService(TestCase):
    def setUp(self):
        self.cliente = Cliente.objects.create(nombre_completo='Cliente 1', direccion='Dirección 1', telefono='12345')
        self.beneficiario = Beneficiario.objects.create(nombre_completo='Beneficiario 1', parentesco='Parentesco 1',
                                                        fecha_nacimiento='2000-01-01', sexo='Femenino')

    def test_create_transferencia(self):
        data = {
            'cliente': self.cliente,
            'beneficiario': self.beneficiario,
            'monto': 100,
            'fecha_transferencia': '2024-01-01',
            'estado': 'pendiente'
        }
        transferencia = TransferenciaService().create_transferencia(**data)
        self.assertIsInstance(transferencia, Transferencia)
        self.assertEqual(transferencia.cliente, self.cliente)
        self.assertEqual(transferencia.beneficiario, self.beneficiario)
        self.assertEqual(transferencia.monto, data['monto'])
        self.assertEqual(str(transferencia.fecha_transferencia), data['fecha_transferencia'])
        self.assertEqual(transferencia.estado, data['estado'])

    def test_update_transferencia(self):
        transferencia = Transferencia.objects.create(cliente=self.cliente, beneficiario=self.beneficiario, monto=100,
                                                     fecha_transferencia='2024-01-01', estado='pendiente')
        updated_data = {'monto': 200}
        updated_transferencia = TransferenciaService().update_transferencia(transferencia, **updated_data)
        self.assertEqual(updated_transferencia.monto, updated_data['monto'])

    def test_delete_transferencia(self):
        transferencia = Transferencia.objects.create(cliente=self.cliente, beneficiario=self.beneficiario, monto=100,
                                                     fecha_transferencia='2024-01-01', estado='pendiente')
        deleted_transferencia = TransferenciaService().delete_transferencia(transferencia)
        self.assertEqual(deleted_transferencia.estado, 'cancelada')

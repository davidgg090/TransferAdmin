from django.core.exceptions import ObjectDoesNotExist
from django.test import TestCase

from ..models import Cliente
from ..services import ClienteService


class TestClienteService(TestCase):
    def setUp(self):
        self.cliente_data = {
            'nombre_completo': 'Juan Pérez',
            'direccion': 'Calle Principal 123',
            'telefono': '123456789'
        }

    def test_create_cliente(self):
        cliente = ClienteService.create_cliente(**self.cliente_data)
        self.assertIsInstance(cliente, Cliente)
        self.assertEqual(cliente.nombre_completo, self.cliente_data['nombre_completo'])

    def test_update_cliente(self):
        cliente = ClienteService.create_cliente(**self.cliente_data)
        updated_data = {'nombre_completo': 'Juan Pérez Actualizado'}
        updated_cliente = ClienteService.update_cliente(cliente, **updated_data)
        self.assertEqual(updated_cliente.nombre_completo, updated_data['nombre_completo'])

    def test_delete_cliente(self):
        cliente = ClienteService.create_cliente(**self.cliente_data)
        ClienteService.delete_cliente(cliente)
        with self.assertRaises(ObjectDoesNotExist):
            Cliente.objects.get(id=cliente.id)

from django.test import TestCase
from django.core.exceptions import ObjectDoesNotExist
from ..services import BeneficiarioService
from ..models import Beneficiario


class TestBeneficiarioService(TestCase):
    def setUp(self):
        self.beneficiario_data = {
            'nombre_completo': 'María López',
            'parentesco': 'Hija',
            'fecha_nacimiento': '2000-01-01',
            'sexo': 'Femenino'
        }

    def test_create_beneficiario(self):
        beneficiario = BeneficiarioService.create_beneficiario(**self.beneficiario_data)
        self.assertIsInstance(beneficiario, Beneficiario)
        self.assertEqual(beneficiario.nombre_completo, self.beneficiario_data['nombre_completo'])

    def test_update_beneficiario(self):
        beneficiario = BeneficiarioService.create_beneficiario(**self.beneficiario_data)
        updated_data = {'nombre_completo': 'María López Actualizado'}
        updated_beneficiario = BeneficiarioService.update_beneficiario(beneficiario, **updated_data)
        self.assertEqual(updated_beneficiario.nombre_completo, updated_data['nombre_completo'])

    def test_delete_beneficiario(self):
        beneficiario = BeneficiarioService.create_beneficiario(**self.beneficiario_data)
        BeneficiarioService.delete_beneficiario(beneficiario)
        with self.assertRaises(ObjectDoesNotExist):
            Beneficiario.objects.get(id=beneficiario.id)

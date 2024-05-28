from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.test import APITestCase

from ..models import Beneficiario


class TestBeneficiarioListCreate(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test_user', password='test_password')
        self.client.force_authenticate(user=self.user)

    def test_create_beneficiario(self):
        url = '/beneficiarios/'
        data = {
            'nombre_completo': 'Test Beneficiario',
            'parentesco': 'Hijo',
            'fecha_nacimiento': '2000-01-01',
            'sexo': 'M'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Beneficiario.objects.count(), 1)
        self.assertEqual(Beneficiario.objects.get().nombre_completo, 'Test Beneficiario')

    def test_list_beneficiarios(self):
        Beneficiario.objects.create(nombre_completo='Beneficiario 1', parentesco='Padre',
                                    fecha_nacimiento='1990-01-01', sexo='M')
        Beneficiario.objects.create(nombre_completo='Beneficiario 2', parentesco='Madre',
                                    fecha_nacimiento='1995-01-01', sexo='F')
        url = '/beneficiarios/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)


class TestBeneficiarioRetrieveUpdateDestroy(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='test_user', password='test_password')
        self.beneficiario = Beneficiario.objects.create(nombre_completo="Beneficiario de Prueba",
                                                        parentesco="Padre",
                                                        fecha_nacimiento="1990-01-01",
                                                        sexo="M")

        response = self.client.post(reverse('token_obtain_pair'), {'username': 'test_user',
                                                                   'password': 'test_password'}, format='json')
        self.token = response.data['access']

    def test_retrieve_beneficiario(self):
        url = reverse('beneficiario-retrieve-update-destroy', kwargs={'pk': self.beneficiario.pk})
        response = self.client.get(url, HTTP_AUTHORIZATION=f'Bearer {self.token}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_beneficiario(self):
        url = reverse('beneficiario-retrieve-update-destroy', kwargs={'pk': self.beneficiario.pk})
        data = {'nombre_completo': 'Beneficiario Actualizado', 'parentesco': 'Madre',
                'fecha_nacimiento': '1995-01-01', 'sexo': 'F'}
        response = self.client.put(url, data, HTTP_AUTHORIZATION=f'Bearer {self.token}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_beneficiario(self):
        url = reverse('beneficiario-retrieve-update-destroy', kwargs={'pk': self.beneficiario.pk})
        response = self.client.delete(url, HTTP_AUTHORIZATION=f'Bearer {self.token}')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

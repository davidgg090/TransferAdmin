from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.test import APITestCase

from ..models import Cliente


class TestClienteListCreate(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test_user', password='test_password')
        self.client.force_authenticate(user=self.user)

    def test_create_cliente(self):
        url = '/clientes/'
        data = {'nombre_completo': 'Test Cliente', 'direccion': 'Test Direccion', 'telefono': '12345'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Cliente.objects.count(), 1)
        self.assertEqual(Cliente.objects.get().nombre_completo, 'Test Cliente')

    def test_list_clientes(self):
        Cliente.objects.create(nombre_completo='Cliente 1', direccion='Dirección 1', telefono='12345')
        Cliente.objects.create(nombre_completo='Cliente 2', direccion='Dirección 2', telefono='67890')
        url = '/clientes/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)


class ClienteRetrieveUpdateDestroyTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='test_user', password='test_password')
        self.cliente = Cliente.objects.create(nombre_completo="Cliente de Prueba", direccion="Dirección de Prueba",
                                              telefono="123456789")

        response = self.client.post(reverse('token_obtain_pair'), {'username': 'test_user',
                                                                   'password': 'test_password'}, format='json')
        self.token = response.data['access']

    def test_retrieve_cliente(self):
        url = reverse('cliente-retrieve-update-destroy', kwargs={'pk': self.cliente.pk})
        response = self.client.get(url, HTTP_AUTHORIZATION=f'Bearer {self.token}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_cliente(self):
        url = reverse('cliente-retrieve-update-destroy', kwargs={'pk': self.cliente.pk})
        data = {'nombre_completo': 'Cliente Actualizado', 'direccion': 'Nueva Dirección', 'telefono': '987654321'}
        response = self.client.put(url, data, HTTP_AUTHORIZATION=f'Bearer {self.token}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_cliente(self):
        url = reverse('cliente-retrieve-update-destroy', kwargs={'pk': self.cliente.pk})
        response = self.client.delete(url, HTTP_AUTHORIZATION=f'Bearer {self.token}')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

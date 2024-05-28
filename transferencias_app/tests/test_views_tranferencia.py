from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from transferencias_app.models import Cliente, Beneficiario, Transferencia


class TransferenciaListCreateTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test_user', password='test_password')
        self.client.force_authenticate(user=self.user)

        self.cliente = Cliente.objects.create(nombre_completo="Cliente de Prueba",
                                              direccion="Dirección de Prueba", telefono="123456789")
        self.beneficiario = Beneficiario.objects.create(nombre_completo="Beneficiario de Prueba",
                                                        parentesco="Amigo", fecha_nacimiento="2000-01-01", sexo="M")

    def test_create_transferencia(self):
        url = reverse('transferencia-list-create')
        data = {
            'cliente': self.cliente.id,
            'beneficiario': self.beneficiario.id,
            'monto': '100.50',
            'fecha_transferencia': '2024-05-27',
            'estado': 'pendiente'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Transferencia.objects.count(), 1)
        self.assertEqual(str(Transferencia.objects.get().monto), '100.50')

    def test_list_transferencias(self):
        Transferencia.objects.create(
            cliente=self.cliente,
            beneficiario=self.beneficiario,
            monto='100.50',
            fecha_transferencia='2024-05-27',
            estado='pendiente'
        )
        Transferencia.objects.create(
            cliente=self.cliente,
            beneficiario=self.beneficiario,
            monto='200.75',
            fecha_transferencia='2024-05-27',
            estado='completada'
        )
        url = reverse('transferencia-list-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)


class TransferenciaRetrieveUpdateDestroyTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='test_user', password='test_password')
        self.client.force_authenticate(user=self.user)

        self.cliente = Cliente.objects.create(nombre_completo="Cliente de Prueba", direccion="Dirección de Prueba",
                                              telefono="123456789")
        self.beneficiario = Beneficiario.objects.create(nombre_completo="Beneficiario de Prueba", parentesco="Amigo",
                                                        fecha_nacimiento="2000-01-01", sexo="M")
        self.transferencia = Transferencia.objects.create(
            cliente=self.cliente,
            beneficiario=self.beneficiario,
            monto='100.50',
            fecha_transferencia='2024-05-27',
            estado='pendiente'
        )

    def test_retrieve_transferencia(self):
        url = reverse('transferencia-detail', kwargs={'pk': self.transferencia.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['monto'], str(self.transferencia.monto))

    def test_update_transferencia(self):
        url = reverse('transferencia-detail', kwargs={'pk': self.transferencia.pk})
        data = {
            'cliente': self.cliente.id,
            'beneficiario': self.beneficiario.id,
            'monto': '200.75',
            'fecha_transferencia': '2024-05-27',
            'estado': 'completada'
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.transferencia.refresh_from_db()
        self.assertEqual(str(self.transferencia.monto), data['monto'])
        self.assertEqual(self.transferencia.estado, data['estado'])

    def test_delete_transferencia(self):
        url = reverse('transferencia-detail', kwargs={'pk': self.transferencia.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.transferencia.refresh_from_db()
        self.assertEqual(self.transferencia.estado, 'cancelada')

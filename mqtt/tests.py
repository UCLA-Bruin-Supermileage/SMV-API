from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Trip

class MyModelAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        self.model_instance = Trip.objects.create(name='Test Item', date_created= '2025-02-05', start= '2025-02-25T18:23:51.491Z', stop= '2025-02-25T18:23:51.491Z')

    def test_create_model_instance(self):
        url = '/api/trip/'  # Adjust based on your router configuration
        data = {'name': 'New Item', 'date_created': '2025-02-05', 'start': '2025-02-25T18:23:51.491Z', 'stop': '2025-02-25T18:23:51.491Z'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Trip.objects.count(), 2)

    def test_get_model_instance(self):
        url = f'/api/trip/{self.model_instance.id}/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test Item')

    def test_list_model_instances(self):
        url = '/api/trip/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_update_model_instance(self):
        url = f'/api/mtripymodel/{self.model_instance.id}/'
        data = {'name': 'Updated Item', 'start': '2025-02-26T18:23:51.491Z'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.model_instance.refresh_from_db()
        self.assertEqual(self.model_instance.name, 'Updated Item')

    def test_delete_model_instance(self):
        url = f'/api/mymodel/{self.model_instance.id}/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Trip.objects.count(), 0)

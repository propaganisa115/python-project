import pytest as pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User


class AuthViewsTests(APITestCase):
    def test_api_jwt(self):
        url = reverse('token_obtain_pair')
        u = User.objects.create(username='user', email='user@foo.com', password='pass')
        u.is_active = False
        u.save()

        resp = self.client.post(url, {'username':'user', 'password':'pass'}, format='json')
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)

        u.is_active = True
        u.save()

        response = self.client.post('/api/token/', data={'username': 'user', 'password': 'pass'},format='json')
        client = APIClient()
        print(response.json())
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + response.json()['access'])
        self.assertEquals(response.status_code, 200)

        resp = self.client.post(url, {'username':'user', 'password':'pass'}, format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertTrue('token' in resp.data)
        token = resp.data['token']
        #print(token)

        verification_url = reverse('token_obtain_pair')
        resp = self.client.post(verification_url, {'token': token}, format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

        resp = self.client.post(verification_url, {'token': 'abc'}, format='json')
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='JWT ' + 'abc')
        resp = client.get('/pesanan', data={'format': 'json'})
        self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)
        client.credentials(HTTP_AUTHORIZATION='JWT ' + token)
        resp = client.get('/keranjang', data={'format': 'json'})
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from ..models import Author
from django.contrib.auth.models import User


class AuthorTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client = APIClient()
        response = self.client.post(reverse('token_obtain_pair'), {'username': 'testuser', 'password': 'testpass'},
                                    format='json')
        self.token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

        self.author1 = Author.objects.create(first_name="Author", last_name="One", birth_date='1990-01-01')
        self.author2 = Author.objects.create(first_name="Author", last_name="Two", birth_date='1990-01-01')

    def test_get_authors_list(self):
        url = reverse('author-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)

    def test_get_author_detail(self):
        url = reverse('author-detail', args=[self.author1.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['first_name'], 'Author')
        self.assertEqual(response.data['last_name'], 'One')

    def test_create_author(self):
        url = reverse('author-list')
        data = {"first_name": "Author", "last_name": "Three", 'birth_date': '1990-01-01'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Author.objects.count(), 3)

    def test_update_author(self):
        url = reverse('author-detail', args=[self.author1.pk])
        data = {'first_name': 'Author', 'last_name': 'One Updated', 'birth_date': '1970-01-01'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Author.objects.get(pk=self.author1.pk).last_name, 'One Updated')

    def test_delete_author(self):
        url = reverse('author-detail', args=[self.author1.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Author.objects.count(), 1)

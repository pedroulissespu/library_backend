from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from ..models import Author


class AuthorTests(TestCase):
    fixtures = ['authors/fixtures/authors.json']

    def test_get_authors_list(self):
        url = reverse('author-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_author_detail(self):
        url = reverse('author-detail', args=[1])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Author One')

    def test_create_author(self):
        url = reverse('author-list')
        data = {'name': 'Author Three', 'birthdate': '1990-01-01'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Author.objects.count(), 3)

    def test_update_author(self):
        url = reverse('author-detail', args=[1])
        data = {'name': 'Author One Updated', 'birthdate': '1970-01-01'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Author.objects.get(pk=1).name, 'Author One Updated')

    def test_delete_author(self):
        url = reverse('author-detail', args=[1])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Author.objects.count(), 1)

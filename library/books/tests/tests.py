from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from ..models import Book


class BookTests(TestCase):
    fixtures = ['books/fixtures/books.json', 'authors/fixtures/authors.json']

    def test_get_books_list(self):
        url = reverse('book-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_book_detail(self):
        url = reverse('book-detail', args=[1])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Book One')

    def test_create_book(self):
        url = reverse('book-list')
        data = {'title': 'Book Three', 'publication_date': '2020-01-01', 'author': 1}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_update_book(self):
        url = reverse('book-detail', args=[1])
        data = {'title': 'Book One Updated', 'publication_date': '2000-01-01', 'author': 1}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.get(pk=1).title, 'Book One Updated')

    def test_delete_book(self):
        url = reverse('book-detail', args=[1])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)
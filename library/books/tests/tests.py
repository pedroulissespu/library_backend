from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from ..models import Book
from ...authors.models import Author


class BookTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client = APIClient()
        response = self.client.post(reverse('token_obtain_pair'), {'username': 'testuser', 'password': 'testpass'},
                                    format='json')
        self.token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

        self.author1 = Author.objects.create(first_name="Author", last_name="One", birth_date='1990-01-01')
        self.author2 = Author.objects.create(first_name="Author", last_name="Two", birth_date='1990-01-01')

        self.book1 = Book.objects.create(title="Book Three", published_date="1999-01-01", isbn='122456789',
                                         page_count=1, language="br", author=self.author1)
        self.book2 = Book.objects.create(title="Book Four", published_date="1999-01-01", isbn='123756789',
                                         page_count=2, language="br", author=self.author2)

    def test_get_books_list(self):
        url = reverse('book-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)

    def test_get_book_detail(self):
        url = reverse('book-detail', args=[self.book1.pk])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Book Three')

    def test_create_book(self):
        url = reverse('book-list')
        data = {"title": "Book Four Updated", "published_date": "1999-01-01", "isbn": '222456789',
                "page_count": 1, "language": "br", "author": self.author1.pk}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_update_book(self):
        url = reverse('book-detail', args=[self.book1.pk])
        data = {"title": "Book Three Updated", "published_date": "1999-01-01", "isbn": '122456789',
                "page_count": 1, "language": "br", "author": self.author1.pk}

        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.get(pk=self.book1.pk).title, 'Book Three Updated')

    def test_delete_book(self):
        url = reverse('book-detail', args=[self.book1.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

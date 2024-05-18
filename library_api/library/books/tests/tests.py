from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from library_api.library.authors.models import Author
from ..models import Book


class BookTests(TestCase):

    def setUp(self):
        self.author = Author.objects.create(first_name="John", last_name="Doe")
        self.book = Book.objects.create(
            title="Test Book",
            author=self.author,
            published_date="2023-01-01",
            isbn="1234567890123",
            page_count=100,
            language="EN"
        )
        self.url = reverse('book-list')

    def test_create_book(self):
        data = {
            "title": "New Book",
            "author": self.author.id,
            "published_date": "2023-01-01",
            "isbn": "1234567890123",
            "page_count": 200,
            "language": "EN"
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
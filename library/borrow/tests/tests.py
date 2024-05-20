from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from ...authors.models import Author
from ...books.models import Book
from ..models import Borrow


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

        self.borrow1 = Borrow.objects.create(user=self.user, book=self.book1, borrow_date="2023-07-01",
                                             return_date=None)
        self.borrow2 = Borrow.objects.create(user=self.user, book=self.book2, borrow_date="2023-05-01",
                                             return_date=None)

    def test_get_retrieve_list(self):
        response = self.client.get(reverse('borrow-list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 4)

    def test_post_create(self):
        data = {
            "user": self.user.pk,
            "book": self.book1.pk,
            "borrow_date": "2024-01-01",
            "return_date": "2024-01-10"
        }
        url = reverse('borrow-list')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Borrow.objects.count(), 3)

    def test_put_update(self):
        data = {
            "user": self.user.pk,
            "book": self.book1.pk,
            "borrow_date": "2024-01-01",
            "return_date": "2025-01-10"
        }
        url = reverse('borrow-detail', args=[self.borrow2.pk])
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, 200)
        borrow = Borrow.objects.get(pk=self.borrow2.pk)
        self.assertEqual(str(borrow.return_date), '2025-01-10')

    def test_patch_partial_update(self):
        data = {
            "return_date": "2025-01-20"
        }
        url = reverse('borrow-detail', args=[self.borrow2.pk])
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, 200)
        borrow = Borrow.objects.get(pk=self.borrow2.pk)
        self.assertEqual(str(borrow.return_date), '2025-01-20')

    def test_delete_destroy(self):
        url = reverse('borrow-detail', args=[self.borrow1.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Borrow.objects.count(), 1)

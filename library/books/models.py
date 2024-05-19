from django.db import models

from library.authors.models import Author


class Book(models.Model):
    objects = models.Manager()

    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13)
    page_count = models.IntegerField()
    language = models.CharField(max_length=2)

    def __str__(self):
        return self.title

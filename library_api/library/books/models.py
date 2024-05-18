from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey('authors.Author', on_delete=models.CASCADE)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13)
    page_count = models.IntegerField()
    cover = models.ImageField(upload_to='covers/', null=True, blank=True)
    language = models.CharField(max_length=2)

    def __str__(self):
        return self.title

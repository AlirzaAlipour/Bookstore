from django.core.validators import MinValueValidator
from django.db import models


# Create your models here.


class Categorie (models.Model):
    title = models.CharField(max_length=255)
    def __str__(self) -> str:
        return self.title
    class Meta:
        ordering = ['title']

class Author (models.Model):
    name = models.CharField(max_length=255)
    def __str__(self) -> str:
        return self.name
    class Meta:
        ordering = ['name']

class Publisher (models.Model):
    title = models.CharField(max_length=255)
    def __str__(self) -> str:
        return self.title
    class Meta:
        ordering = ['title']


class Book (models.Model):
    title = models.CharField(max_length=255)
    publisher = models.ForeignKey(Publisher, on_delete=models.PROTECT)
    author = models.ManyToManyField(Author)
    categorie = models.ForeignKey(Categorie, on_delete=models.PROTECT)
    description = models.TextField(max_length=1024, null=True, blank=True)
    price = models.IntegerField()
    def __str__(self) -> str:
        return self.title
    class Meta:
        ordering = ['title']



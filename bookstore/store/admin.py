from typing import Any
from django.contrib import admin
from django.db.models.aggregates import Count
from django.db.models.query import QuerySet
from django.utils.html import format_html , urlencode
from django.urls import reverse
from django.http import HttpRequest
from . import models

@admin.register(models.Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ["title", "book_count"]
    
    @admin.display(ordering="book_count")
    def book_count(self, categorie):
        url = (
            reverse('admin:store_categorie_changelist')
            + '?'
            + urlencode({
                'categorie__id': str(categorie.id)
            }))
        return format_html('<a href="{}">{}</a>', url, categorie.book_count)
    
    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        return super().get_queryset(request).annotate(
            book_count=Count("book")
        )


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["title","publisher","categorie_title","price"]
    list_select_related = ["categorie"]
    def categorie_title(self, book):
        return book.categorie.title
    

admin.site.register(models.Author)
admin.site.register(models.Publisher)



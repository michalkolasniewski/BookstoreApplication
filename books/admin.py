from django.contrib import admin

from books.models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'authors', 'published_date', 'page_count']
    fields = ['title',
              'authors',
              'published_date',
              'page_count',
              'print_type',
              'categories',
              'average_rating',
              'ratings_count',
              'language',
              'country',
              'saleability',
              'is_ebook',
              'type',
              'identifier',
              'text',
              'image',
              'is_pdf',
              'is_epub',
    ]

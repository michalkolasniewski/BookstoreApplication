from rest_framework import serializers

from books.models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id',
                  'title',
                  'authors',
                  'published_date',
                  'page_count',
                  'print_type',
                  'categories',
                  'average_rating',
                  'ratings_count',
                  'language',
                  'sale_info',
                  'reading_modes',
                  'industry_identifiers',
                  'is_pdf',
                  'is_epub',
                  ]


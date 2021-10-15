from rest_framework import serializers

from books.models import Book, SaleInfo, ReadingModes, IndustryIdentifiers


class ReadingModesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReadingModes
        fields = '__all__'


class SaleInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleInfo
        fields = '__all__'


class IndustryIdentifiersSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndustryIdentifiers
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'authors', 'published_date', 'page_count', 'average_rating']


class DetailBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id',
                  'title',
                  'authors',
                  'published_date',
                  'page_count',
                  'print_type',
                  'average_rating',
                  'ratings_count',
                  'language',
                  'sale_info',
                  'reading_modes',
                  'industry_identifiers',
                  'opinion'
                  ]

    sale_info = SaleInfoSerializer(many=True)
    reading_modes = ReadingModesSerializer(many=True)
    industry_identifiers = IndustryIdentifiersSerializer(many=True)
    opinion = serializers.SerializerMethodField()

    def get_opinion(self, obj):
        if obj.average_rating > 3:
            return f'Książka warta przeczytania'
        else:
            return f'Nie warto przeczytać'

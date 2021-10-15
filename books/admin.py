from django.contrib import admin

# Register your models here.
from books.models import IndustryIdentifiers, SaleInfo, Book, ReadingModes


@admin.register(IndustryIdentifiers)
class IndustryIdentifiersAdmin(admin.ModelAdmin):
    pass


@admin.register(ReadingModes)
class ReadingModesAdmin(admin.ModelAdmin):
    pass


@admin.register(SaleInfo)
class SaleInfoAdmin(admin.ModelAdmin):
    pass


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    fields = [
        ('title',
         'authors',
         'published_date',
         'industry_identifiers',
         'reading_modes',
         'page_count',
         'print_type',
         'average_rating',
         'ratings_count',
         'language',
         'sale_info')
    ]

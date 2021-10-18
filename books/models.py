from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

NOT_FOR_SALE = 'NOT_FOR_SALE'
FOR_SALE = 'FOR_SALE'

SALEABILITY = [
    (NOT_FOR_SALE, 'NOT_FOR_SALE'),
    (FOR_SALE, 'FOR_SALE')
]
NONE = 'NONE'
HISTORY = 'HISTORY'
FANTASY = 'FANTASY'

CATEGORIES = [
    (NONE, 'NONE'),
    (HISTORY, 'HISTORY'),
    (FANTASY, 'FANTASY')
]


class Book(models.Model):
    country = models.CharField(max_length=10, verbose_name='kraj')
    saleability = models.CharField(max_length=12, choices=SALEABILITY, default=FOR_SALE)
    is_ebook = models.BooleanField(verbose_name='ebook')

    type = models.CharField(max_length=150, verbose_name='typ')
    identifier = models.CharField(max_length=150, verbose_name='identyfikator')

    text = models.BooleanField(verbose_name='tekst')
    image = models.BooleanField(verbose_name='obrazek')

    title = models.CharField(max_length=300, verbose_name='tytuł')
    authors = models.CharField(max_length=450, verbose_name='autorzy')
    published_date = models.DateField(verbose_name='data publikacji')

    page_count = models.SmallIntegerField(verbose_name='liczba stron')
    print_type = models.CharField(max_length=15, verbose_name='typ wydruku')
    average_rating = models.SmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(6)], verbose_name='średnia ocena')
    ratings_count = models.SmallIntegerField(verbose_name='liczba ocen')
    language = models.CharField(max_length=5, verbose_name='język')
    categories = models.CharField(max_length=20, choices=CATEGORIES, default=NONE)
    is_epub = models.BooleanField(verbose_name='epub')
    is_pdf = models.BooleanField(verbose_name='pdf')

    @property
    def epub(self):
        return {'isAvailable': self.is_epub}

    @property
    def pdf(self):
        return {'isAvailable': self.is_pdf}

    @property
    def sale_info(self):
        return {'saleability': self.saleability, 'country': self.country, 'is_ebook': self.is_ebook}

    @property
    def industry_identifiers(self):
        return {'type': self.type, 'identifier': self.identifier}

    @property
    def reading_modes(self):
        return {'text': self.text, 'image': self.image}

    def __str__(self):
        return f'{self.title}, {self.authors}'

    class Meta:
        verbose_name = 'książka'
        verbose_name_plural = 'książki'

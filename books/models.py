from django.db import models


class IndustryIdentifiers(models.Model):
    type = models.CharField(max_length=150, verbose_name='typ')
    identifier = models.CharField(max_length=150, verbose_name='identyfikator')

    def __str__(self):
        return f'{self.type}'

    class Meta:
        verbose_name = 'identyfikator branżowy'
        verbose_name_plural = 'identyfikatory branżowe'


class ReadingModes(models.Model):
    text = models.BooleanField(verbose_name='tekst')
    image = models.BooleanField(verbose_name='obrazek')

    def __str__(self):
        return f'{self.text}, {self.image}'

    class Meta:
        verbose_name = 'tryb czytania'
        verbose_name_plural = 'tryby czytania'


NOT_FOR_SALE = 'NOT_FOR_SALE'
FOR_SALE = 'FOR_SALE'

SALEABILITY = [
    (NOT_FOR_SALE, 'NOT_FOR_SALE'),
    (FOR_SALE, 'FOR_SALE')
]


class SaleInfo(models.Model):
    country = models.CharField(max_length=10, verbose_name='kraj')
    saleability = models.CharField(max_length=12, choices=SALEABILITY, default=FOR_SALE)
    is_ebook = models.BooleanField(verbose_name='ebook')

    def __str__(self):
        return f'{self.country}, {self.saleability}'

    class Meta:
        verbose_name = 'informacja o sprzedaży'
        verbose_name_plural = 'informacje o sprzedaży'


class Book(models.Model):
    title = models.CharField(max_length=300, verbose_name='tytuł')
    authors = models.CharField(max_length=450, verbose_name='autorzy')
    published_date = models.DateField(verbose_name='data publikacji')
    industry_identifiers = models.ManyToManyField(IndustryIdentifiers, verbose_name='identyfikator branżowy')
    reading_modes = models.ManyToManyField(ReadingModes, verbose_name='tryb czytania')
    page_count = models.SmallIntegerField(verbose_name='liczba stron')
    print_type = models.CharField(max_length=15, verbose_name='typ wydruku')
    average_rating = models.SmallIntegerField(verbose_name='średnia ocena')
    ratings_count = models.SmallIntegerField(verbose_name='liczba ocen')
    language = models.CharField(max_length=5, verbose_name='język')
    sale_info = models.ManyToManyField(SaleInfo, verbose_name='informacja o sprzedaży')


    def __str__(self):
        return f'{self.title}, {self.authors}'

    class Meta:
        verbose_name = 'książka'
        verbose_name_plural = 'książki'
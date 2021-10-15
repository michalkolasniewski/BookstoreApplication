# Generated by Django 3.2.8 on 2021-10-15 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name': 'książka', 'verbose_name_plural': 'książki'},
        ),
        migrations.AlterModelOptions(
            name='industryidentifiers',
            options={'verbose_name': 'identyfikator branżowy', 'verbose_name_plural': 'identyfikatory branżowe'},
        ),
        migrations.AlterModelOptions(
            name='readingmodes',
            options={'verbose_name': 'tryb czytania', 'verbose_name_plural': 'tryby czytania'},
        ),
        migrations.AlterModelOptions(
            name='saleinfo',
            options={'verbose_name': 'informacja o sprzedaży', 'verbose_name_plural': 'informacje o sprzedaży'},
        ),
    ]

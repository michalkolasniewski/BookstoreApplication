from django.core.management.base import BaseCommand

from books.utils import create_random_books, get_dates_from_user


class Command(BaseCommand):
    help = 'Generuje losowe książki'

    def add_arguments(self, parser):
        parser.add_argument('orders_count', type=int, help='Liczba losowo wygenerowanych książek')

    def handle(self, *args, **kwargs):
        orders_count = kwargs['orders_count']
        start_date, end_date = get_dates_from_user()
        create_random_books(orders_count, start_date, end_date)

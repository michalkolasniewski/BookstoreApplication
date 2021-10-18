import random
import string
from datetime import datetime, timedelta

from books.models import Book, CATEGORIES, SALEABILITY


def get_random_saleability():
    random_saleability = random.choice(SALEABILITY)
    return random_saleability


def get_random_category():
    random_category = random.choice(CATEGORIES)
    return random_category


def get_random_language():
    language = ['pl', 'de', 'en', 'es', 'lt', 'ru']
    random_language = random.choice(language)
    return random_language


def get_random_country():
    countries = ['Polska', 'Niemcy', 'Anglia', 'Holandia', 'USA', 'Kanada', 'Francja', 'Włochy']
    random_conutry = random.choice(countries)
    return random_conutry


def get_random_date(start_date, end_date):
    """
    Generuje losową datę
    """
    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.strptime(end_date, '%Y-%m-%d')
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + timedelta(days=random_number_of_days)
    return random_date


def get_dates_from_user():
    """
    Pobiera od użytkownika dane potrzebne do wygenerowania zakresu dat
    w celu wywołania funkcji get_random_date
    """
    while True:
        start_date = input('Podaj datę startową (YYYY-MM-DD)')
        end_date = input('Podaj datę końcową (YYYY-MM-DD)')
        try:
            get_random_date(start_date, end_date)
            if start_date < end_date:
                break
        except ValueError:
            print('Podano niepoprawny format daty lub data początkowa jest późniejsza od końcowej')
    return start_date, end_date


def get_print_type():
    print_type = ['BOOK', 'EBOOK']
    random_print_type = random.choice(print_type)

    return random_print_type


def get_random_author():
    random_first_name = ''.join([random.choice(string.ascii_lowercase) for x in range(10)])
    random_last_name = ''.join([random.choice(string.ascii_lowercase) for x in range(10)])

    return random_first_name.capitalize() + ' ' + random_last_name.capitalize()


def get_random_title():
    title = ['Zaklinacz Czasu', 'Mechaniczny Anioł', 'Cudownie tu i teraz', 'Miasto Kości', 'Igrzyska Śmierci', 'Stowarzyszenie Umarłych Poetów', 'Niecierpliwość serca', 'Nie ma orchidei dla panny Blandish', 'Lot nad kukułczym gniazdem', 'Pod osłoną nieba', 'Stracone zachody miłości', 'Nasz człowiek w Hawanie', 'Dopóki mamy twarze', 'Kochanie, zabiłam nasze koty', 'Jutra może nie być', 'Niech Bóg sprawi, żeby istniał Bóg']
    random_title = random.choice(title)

    return random_title


def create_random_books(books_count, start_date, end_date):
    for x in range(0, books_count):
        published_date = get_random_date(start_date, end_date)

        Book.objects.create(
            country=get_random_country(),
            saleability=get_random_saleability(),
            is_ebook=random.choice([True, False]),
            type=''.join([random.choice(string.ascii_lowercase) for x in range(10)]).capitalize(),
            identifier=''.join([random.choice(string.digits) for x in range(10)]),
            text=random.choice([True, False]),
            image=random.choice([True, False]),
            title=get_random_title(),
            authors=get_random_author(),
            published_date=published_date,
            page_count=321,
            print_type=get_print_type(),
            average_rating=random.randrange(1, 6),
            ratings_count=random.randrange(1, 156),
            language=get_random_language(),
            categories=get_random_category(),
            is_epub=random.choice([True, False]),
            is_pdf=random.choice([True, False])
        )





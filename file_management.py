import json
from book_management import books
from lending_management import lent_books

BOOKS_FILE = 'data/books.json'
LENT_BOOKS_FILE = 'data/lent_books.json'

def load_data():
    try:
        with open(BOOKS_FILE, 'r') as f:
            books.extend(json.load(f))
    except FileNotFoundError:
        pass

    try:
        with open(LENT_BOOKS_FILE, 'r') as f:
            lent_books.extend(json.load(f))
    except FileNotFoundError:
        pass

def save_data():
    with open(BOOKS_FILE, 'w') as f:
        json.dump(books, f, indent=2)
    with open(LENT_BOOKS_FILE, 'w') as f:
        json.dump(lent_books, f, indent=2)

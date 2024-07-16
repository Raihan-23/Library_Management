import json

books = []

def add_book():
    title = input("Enter book title: ")
    authors = input("Enter authors (comma separated): ").split(',')
    isbn = input("Enter ISBN: ")
    year = input("Enter publishing year: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))

    book = {
        "title": title,
        "authors": authors,
        "isbn": isbn,
        "year": year,
        "price": price,
        "quantity": quantity
    }
    books.append(book)
    print(f"Book '{title}' added successfully!")
    save_data()

def view_books():
    if not books:
        print("No books available.")
        return
    for book in books:
        print(json.dumps(book, indent=2))

def search_books():
    search_term = input("Enter title or ISBN to search: ").lower()
    results = [book for book in books if search_term in book['title'].lower() or search_term in book['isbn']]
    if not results:
        print("No books found.")
    for book in results:
        print(json.dumps(book, indent=2))

def search_books_by_author():
    search_term = input("Enter author name to search: ").lower()
    results = [book for book in books if any(search_term in author.lower() for author in book['authors'])]
    if not results:
        print("No books found.")
    for book in results:
        print(json.dumps(book, indent=2))

def remove_book():
    search_term = input("Enter title or ISBN to remove: ").lower()
    global books
    books = [book for book in books if search_term not in book['title'].lower() and search_term not in book['isbn']]
    print(f"Books matching '{search_term}' removed.")
    save_data()

def save_data():
    with open('data/books.json', 'w') as f:
        json.dump(books, f, indent=2)

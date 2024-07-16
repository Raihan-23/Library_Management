import json
from book_management import books, save_data

lent_books = []

def lend_book():
    isbn = input("Enter ISBN of the book to lend: ")
    borrower = input("Enter borrower name: ")
    for book in books:
        if book['isbn'] == isbn:
            if book['quantity'] > 0:
                book['quantity'] -= 1
                lent_books.append({"isbn": isbn, "borrower": borrower})
                print(f"Book '{book['title']}' lent to {borrower}.")
                save_data()
                save_lent_data()
                return
            else:
                print("Not enough books available to lend.")
                return
    print("Book not found.")

def view_lent_books():
    if not lent_books:
        print("No books are currently lent out.")
        return
    for record in lent_books:
        print(record)

def return_book():
    isbn = input("Enter ISBN of the book to return: ")
    borrower = input("Enter borrower name: ")
    for record in lent_books:
        if record['isbn'] == isbn and record['borrower'] == borrower:
            lent_books.remove(record)
            for book in books:
                if book['isbn'] == isbn:
                    book['quantity'] += 1
                    print(f"Book '{book['title']}' returned by {borrower}.")
                    save_data()
                    save_lent_data()
                    return
    print("Record not found.")

def save_lent_data():
    with open('data/lent_books.json', 'w') as f:
        json.dump(lent_books, f, indent=2)

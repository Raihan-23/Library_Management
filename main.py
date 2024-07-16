from book_management import add_book, view_books, search_books, remove_book, search_books_by_author
from lending_management import lend_book, view_lent_books, return_book
from file_management import load_data, save_data

def main():
    load_data()
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Books by Title or ISBN")
        print("4. Search Books by Author")
        print("5. Remove Book")
        print("6. Lend Book")
        print("7. View Lent Books")
        print("8. Return Book")
        print("9. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_book()
        elif choice == '2':
            view_books()
        elif choice == '3':
            search_books()
        elif choice == '4':
            search_books_by_author()
        elif choice == '5':
            remove_book()
        elif choice == '6':
            lend_book()
        elif choice == '7':
            view_lent_books()
        elif choice == '8':
            return_book()
        elif choice == '9':
            save_data()
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

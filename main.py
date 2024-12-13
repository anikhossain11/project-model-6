from utils.view_books import view_books
from utils.add_book import add_book
from utils.lend_book import lend_book
from utils.return_book import return_book

def main():
    while True:
        print("\nLibrary Management System")
        print("1. View Books")
        print("2. Add a Book")
        print("3. Lend a Book")
        print("4. Return a Book")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            view_books()
        elif choice == '2':
            add_book()
        elif choice == '3':
            lend_book()
        elif choice == '4':
            return_book()
        elif choice == '5':
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

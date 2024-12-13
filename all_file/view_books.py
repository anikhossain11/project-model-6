from .file_operations import get_books

def view_books():
    books = get_books()
    if not books:
        print("No books available.")
    else:
        print("\nAvailable Books:")
        for title, author, quantity in books:
            print(f"Title: {title}, Author: {author}, Quantity: {quantity}")

from .file_operations import get_books, save_books

def add_book():
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    quantity = input("Enter quantity: ")

    books = get_books()
    for i, (b_title, b_author, b_quantity) in enumerate(books):
        if b_title == title:
            books[i] = (title, b_author, str(int(b_quantity) + int(quantity)))
            break
    else:
        books.append((title, author, quantity))

    save_books(books)
    print(f"Book '{title}' added successfully!")

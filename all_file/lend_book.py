from datetime import datetime, timedelta
from .file_operations import get_books, save_books, get_lend_records, save_lend_records

def lend_book():
    books = get_books()
    lend_records = get_lend_records()

    title = input("Enter the title of the book to lend: ")
    borrower_name = input("Enter borrower's name: ")
    phone = input("Enter borrower's phone number: ")

    for i, (b_title, b_author, b_quantity) in enumerate(books):
        if b_title == title:
            if int(b_quantity) > 0:
                due_date = (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d")
                lend_records.append({"borrower_name": borrower_name, "phone": phone, "title": title, "due_date": due_date})
                books[i] = (b_title, b_author, str(int(b_quantity) - 1))
                save_books(books)
                save_lend_records(lend_records)
                print(f"Book '{title}' lent successfully to {borrower_name}. Due date: {due_date}.")
                return
            print("There are not enough books available to lend.")
            return
    print(f"Book '{title}' not found.")

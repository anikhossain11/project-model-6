from .file_operations import get_books, save_books, get_lend_records, save_lend_records

def return_book():
    books = get_books()
    lend_records = get_lend_records()

    title = input("Enter the title of the book to return: ")
    borrower_name = input("Enter borrower's name: ")

    for i, record in enumerate(lend_records):
        if record["title"] == title and record["borrower_name"] == borrower_name:
            for j, (b_title, b_author, b_quantity) in enumerate(books):
                if b_title == title:
                    books[j] = (b_title, b_author, str(int(b_quantity) + 1))
                    break
            lend_records.pop(i)
            save_books(books)
            save_lend_records(lend_records)
            print(f"Book '{title}' returned successfully by {borrower_name}.")
            return
    print(f"No record found for '{title}' borrowed by {borrower_name}.")

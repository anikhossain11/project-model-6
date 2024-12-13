import json

BOOKS_FILE = "books.json"
LEND_RECORDS_FILE = "lend_records.json"

def get_books():
    try:
        with open(BOOKS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_books(books):
    with open(BOOKS_FILE, "w") as file:
        json.dump(books, file)

def get_lend_records():
    try:
        with open(LEND_RECORDS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_lend_records(lend_records):
    with open(LEND_RECORDS_FILE, "w") as file:
        json.dump(lend_records, file)

import csv
import os

FILE_NAME = "books.csv"

def main():

    books = load_books(FILE_NAME)

    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":

            book_id = input("Enter book id: ").strip()
            if any(b["id"] == book_id for b in books):
                print("\nThis book already exists!\n")
                continue
            
            title = input("Enter book title: ").strip()
            author = input("Enter author name: ").strip()
            year = input("Enter year of publish: ").strip()
            count = input("Enter count of book: ").strip()

            
            if add_book(books, book_id, title, author, year, count):
                save_books(FILE_NAME, books)
                print("\nBook added successfully!\n")
            else:
                print("\nFailed to add book. Please check your inputs (Year and Count must be numbers)\n")

        elif choice == "2":
            show_books(books)

        elif choice == "3":
            query = input("Enter book title or id: ").strip()
            result = search_book(books, query)
            if result:
                print("Your search result: ")
                print(f"ID: {result['id']} | Title: {result['title']} | Author: {result['author']} | Year: {result['year']} | Count: {result['count']}")
                print("----------------------------------\n")
            else:
                print("\nBook not found!\n")

        elif choice == "4":
            book_id = input("Enter book id: ").strip()

            if not any(b["id"] == book_id for b in books):
                print("\nBook not found!\n")
                continue

            new_title = input("Enter new title: ").strip()
            new_author = input("Enter new author: ").strip()
            new_year = input("Enter new year: ").strip()
            new_count = input("Enter new count: ").strip()

            if edit_book(books, book_id, new_title, new_author, new_year, new_count):
                save_books(FILE_NAME, books)
                print("\nBook updated successfully\n")
            else:
                print("\nUpdate failed. Invalid inputs.\n")

        elif choice == "5":
            book_id = input("Enter book id: ").strip()
            if delete_book(books, book_id):
                save_books(FILE_NAME, books)
                print(f"\nBook with ID {book_id} deleted successfully!\n")
            else:
                print("\nBook not found!\n")

        elif choice == "6":
            print("End of program. Goodbye!")
            break
        else:
            print("\nInvalid choice! Please try again.\n")


def show_menu():
    print("---- Library Management System ---- ")
    print("1) Add a new book")
    print("2) Show all books")
    print("3) Search for a book")
    print("4) Edit book information")
    print("5) Delete book")
    print("6) Exit")


def load_books(filename):
    """Load books from CSV file."""
    books = []
    if not os.path.exists(filename):
        return books
    try:
        with open(filename, mode="r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                books.append(row)
    except csv.Error:
        print("CSV file is corrupted or invalid.")
        
    return books


def save_books(filename, books):
    """Save books in CSV file."""
    with open(filename, mode="w", newline="", encoding="utf-8") as f:
        fieldnames = ["id", "title", "author", "year", "count"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(books)


def add_book(books_list, book_id, title, author, year, count):
    """Add a new book after validating the inputs."""
    if not book_id or not title or not author:
        return False
    
    if not year.isdigit() or not count.isdigit():
        return False
    
    new_book = {
        "id": book_id,
        "title": title,
        "author": author,
        "year": year,
        "count": count
    }
    books_list.append(new_book)
    return True


def show_books(books_list):
    """Show list of books."""
    if not books_list:
        print("No books in the library!\n")
        return
    print("--- Books List ---")
    for b in books_list:
        print(f"ID: {b['id']} | Title: {b['title']} | Author: {b['author']} | Year: {b['year']} | Count: {b['count']}")
    print("------------------\n")


def search_book(books_list, query):
    """Search book by its ID or name. """
    query = query.lower()
    for b in books_list:
        if b["id"].lower() == query or b["title"].lower() == query:
            return b
    return None


def edit_book(books_list, book_id, title, author, year, count):
    """Edit an existing book's information with validation for new values."""
    if not title or not author or not year.isdigit() or not count.isdigit():
        return False
    
    for b in books_list:
        if b["id"] == book_id:
            b["title"] = title
            b["author"] = author
            b["year"] = year
            b["count"] = count
            return True
    return False


def delete_book(books_list, book_id):
    """Delete book by its ID."""
    for b in books_list:
        if b["id"] == book_id:
            books_list.remove(b)
            return True
    return False


if __name__ == "__main__":
    main()

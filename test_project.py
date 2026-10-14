from project import add_book, search_book, edit_book, delete_book


def test_add_book():
    books = []

    assert add_book(books, "1", "Python Basics", "John Smith", "2024", "3") is True
    assert len(books) == 1
    assert books[0]["title"] == "Python Basics"

    assert add_book(books, "", "Test Book", "Author", "2024", "2") is False
    assert add_book(books, "2", "", "Author", "2024", "2") is False
    assert add_book(books, "2", "Test Book", "Author", "year", "2") is False
    assert add_book(books, "2", "Test Book", "Author", "2024", "two") is False


def test_search_book():
    books = [
        {
            "id": "1",
            "title": "Python Basics",
            "author": "John Smith",
            "year": "2024",
            "count": "3"
        }
    ]

    assert search_book(books, "1") == books[0]
    assert search_book(books, "python basics") == books[0]
    assert search_book(books, "PYTHON BASICS") == books[0]
    assert search_book(books, "Unknown Book") is None


def test_edit_book():
    books = [
        {
            "id": "1",
            "title": "Old Title",
            "author": "Old Author",
            "year": "2020",
            "count": "1"
        }
    ]

    assert edit_book(books, "1", "New Title", "New Author", "2024", "5") is True
    assert books[0]["title"] == "New Title"
    assert books[0]["author"] == "New Author"
    assert books[0]["year"] == "2024"
    assert books[0]["count"] == "5"

    assert edit_book(books, "1", "", "Author", "2024", "2") is False
    assert edit_book(books, "1", "Title", "Author", "year", "2") is False
    assert edit_book(books, "99", "Title", "Author", "2024", "2") is False


def test_delete_book():
    books = [
        {
            "id": "1",
            "title": "Python Basics",
            "author": "John Smith",
            "year": "2024",
            "count": "3"
        },
        {
            "id": "2",
            "title": "CS50",
            "author": "David Malan",
            "year": "2023",
            "count": "2"
        }
    ]

    assert delete_book(books, "1") is True
    assert len(books) == 1
    assert books[0]["id"] == "2"

    assert delete_book(books, "99") is False

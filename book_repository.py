import unittest

class Book:
    def __init__(self, book_id, title, author, isbn):
        self.id = book_id
        self.title = title
        self.author = author
        self.isbn = isbn

class BookRepository:
    def __init__(self):
        self.books = []

    def save(self, book: Book):
        self.books.append(book)
        return book

    def find_by_isbn(self, isbn: str):
        for b in self.books:
            if b.isbn == isbn:
                return b
        return None

class TestBookRepository(unittest.TestCase):
    def test_save_book(self):
        # 1. Arrange
        repo = BookRepository()
        book = Book(1, "Clean Code", "Robert C. Martin", "9780132350884")
        # 2. Act
        repo.save(book)
        # 3. Assert
        self.assertEqual(len(repo.books), 1)

    def test_find_by_isbn(self):
        # 1. Arrange
        repo = BookRepository()
        repo.save(Book(1, "Clean Code", "Robert C. Martin", "9780132350884"))
        # 2. Act
        found = repo.find_by_isbn("9780132350884")
        # 3. Assert
        self.assertIsNotNone(found)
        self.assertEqual(found.title, "Clean Code")

if __name__ == "__main__":
    unittest.main()
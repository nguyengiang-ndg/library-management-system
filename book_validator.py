import unittest

class BookValidator:
    def is_valid_isbn(self, isbn: str) -> bool:
        clean_isbn = isbn.replace("-", "").strip()
        return clean_isbn.isdigit() and len(clean_isbn) in (10, 13)

class TestBookValidator(unittest.TestCase):
    def test_valid_isbn(self):
        # 1. Arrange
        validator = BookValidator()
        # 2. Act
        result = validator.is_valid_isbn("978-604-2-12345-6")
        # 3. Assert
        self.assertTrue(result)

    def test_invalid_isbn(self):
        # 1. Arrange
        validator = BookValidator()
        # 2. Act
        result = validator.is_valid_isbn("ABC-12345")
        # 3. Assert
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()
import unittest

# --- CODE LOGIC (TASK T3 & HOẠT ĐỘNG 3) ---
class FineCalculator:
    def calculate(self, days_overdue: int) -> float:
        if days_overdue <= 0:
            return 0
        fine = days_overdue * 5000
        if days_overdue > 10:
            fine = fine * 1.2
        return fine

class BookService:
    def __init__(self):
        self.existing_isbns = set()

    def add_book(self, title: str, author: str, isbn: str) -> bool:
        if isbn in self.existing_isbns:
            raise ValueError("ISBN đã tồn tại trong hệ thống!")
        self.existing_isbns.add(isbn)
        return True

# --- UNIT TEST THEO CẤU TRÚC AAA (TASK T5 & HOẠT ĐỘNG 3) ---
class TestLeaderTasks(unittest.TestCase):
    def test_no_fine(self):
        # 1. Arrange
        calc = FineCalculator()
        # 2. Act
        actual = calc.calculate(0)
        # 3. Assert
        self.assertAlmostEqual(actual, 0, places=2)

    def test_normal_fine(self):
        # 1. Arrange
        calc = FineCalculator()
        # 2. Act
        actual = calc.calculate(5)
        # 3. Assert
        self.assertAlmostEqual(actual, 25000, places=2)

    def test_heavy_fine(self):
        # 1. Arrange
        calc = FineCalculator()
        # 2. Act
        actual = calc.calculate(11)
        # 3. Assert
        self.assertAlmostEqual(actual, 66000, places=2)

    def test_add_book_success(self):
        # 1. Arrange
        service = BookService()
        # 2. Act
        result = service.add_book("Nhập môn CNPM", "Tác giả A", "1112223339")
        # 3. Assert
        self.assertTrue(result)

    def test_add_book_duplicate_isbn(self):
        # 1. Arrange
        service = BookService()
        service.add_book("Nhập môn CNPM", "Tác giả A", "1112223339")
        # 2. Act & 3. Assert
        with self.assertRaises(ValueError):
            service.add_book("Sách Khác", "Tác giả B", "1112223339")

if __name__ == "__main__":
    unittest.main()
    
import unittest


class UIHelper:
    def format_book_title(self, raw_title: str) -> str:
        if not raw_title or not raw_title.strip():
            return ""
        return " ".join(raw_title.strip().split()).title()


class TestUIHelper(unittest.TestCase):
    def test_format_messy_title(self):
        # 1. Arrange
        helper = UIHelper()
        # 2. Act
        formatted = helper.format_book_title("   lập   trình   python  ")
        # 3. Assert
        self.assertEqual(formatted, "Lập Trình Python")

    def test_format_empty_title(self):
        # 1. Arrange
        helper = UIHelper()
        # 2. Act
        formatted = helper.format_book_title("     ")
        # 3. Assert
        self.assertEqual(formatted, "")


if __name__ == "__main__":
    unittest.main()


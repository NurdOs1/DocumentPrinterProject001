# tests/test_document.py
import unittest
from unittest.mock import MagicMock
from src.document import Document
from src.printers import InkjetPrinter, LaserPrinter

class TestPrinting(unittest.TestCase):

    def setUp(self):
        self.pages = ["Страница 1", "Страница 2", "Страница 3"]
        self.document = Document(self.pages)

    def test_inkjet_printer(self):
        inkjet_printer = InkjetPrinter()
        inkjet_printer.print_page = MagicMock()

        self.document.print_document(inkjet_printer)

        self.assertEqual(inkjet_printer.print_page.call_count, len(self.pages))
        inkjet_printer.print_page.assert_any_call("Страница 1")
        inkjet_printer.print_page.assert_any_call("Страница 2")
        inkjet_printer.print_page.assert_any_call("Страница 3")

    def test_laser_printer(self):
        laser_printer = LaserPrinter()
        laser_printer.print_page = MagicMock()

        self.document.print_document(laser_printer)

        self.assertEqual(laser_printer.print_page.call_count, len(self.pages))
        laser_printer.print_page.assert_any_call("Страница 1")
        laser_printer.print_page.assert_any_call("Страница 2")
        laser_printer.print_page.assert_any_call("Страница 3")

if __name__ == "__main__":
    unittest.main()

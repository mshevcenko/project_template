import unittest
import pandas as pd
from app.io.input import read_text_from_file, read_csv_from_file_with_pandas


class ReadTextFromFileTest(unittest.TestCase):

    def test_read_from_file(self):
        text = read_text_from_file("../../test_data/test.txt")
        self.assertEqual("Hello world!", text)

    def test_read_from_empty_file(self):
        with self.assertRaises(FileNotFoundError):
            read_text_from_file("../../test_data/empty.csv")

    def test_read_from_non_existent_file(self):
        with self.assertRaises(FileNotFoundError):
            read_text_from_file("../../test_data/non_existent.csv")

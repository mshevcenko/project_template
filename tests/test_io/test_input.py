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


class ReadCsvFromFileWithPandasTest(unittest.TestCase):

    def test_read_from_file(self):
        data = read_csv_from_file_with_pandas("../../test_data/test.csv")
        dict_from_file = data.to_dict()
        self.assertEqual({'Name': {0: 'January', 1: 'February', 2: 'March'},
                          'Abbreviation': {0: 'Jan.', 1: 'Feb.', 2: 'Mar.'}}, dict_from_file)

    def test_read_from_empty_file(self):
        with self.assertRaises(pd.errors.EmptyDataError):
            read_csv_from_file_with_pandas("../../test_data/empty.csv")

    def test_read_from_non_existent_file(self):
        with self.assertRaises(FileNotFoundError):
            read_csv_from_file_with_pandas("../../test_data/non_existent.csv")

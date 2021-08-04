import unittest
from src.data_processing import preprocess_dataset
from src.utils import get_highly_correlated_column_names, get_numeric_column_names
import pandas as pd


class DataProcessingTestCase(unittest.TestCase):
    def test_input_none_raises_value_error(self):
        with self.assertRaises(ValueError):
            preprocess_dataset(None)

    def test_input_empty_raises_key_error(self):
        df = pd.DataFrame()
        # the data frame doesn't have the 'q_OpeningHours' column
        with self.assertRaises(KeyError):
            preprocess_dataset(df)

    def test_no_highly_correlated_rows_raises_key_error(self):
        data = {'q_OpeningHours': [7]}
        df = pd.DataFrame.from_dict(data)
        # it will be missing the highly correlated rows
        with self.assertRaises(KeyError):
            preprocess_dataset(df)

    def test_valid_data_success(self):
        data1 = {key: [i, i] for i, key in enumerate(get_highly_correlated_column_names())}
        data2 = {key: [i, i] for i, key in enumerate(get_numeric_column_names())}
        data = {**data1, **data2, 'q_OpeningHours': [7, 7], 'converted': [1, 1]}
        df = pd.DataFrame.from_dict(data)
        # it will be missing the highly correlated rows
        x, y, x_test, y_test = preprocess_dataset(df)
        self.assertIsNotNone(x)
        self.assertIsNotNone(y)
        self.assertIsNotNone(x_test)
        self.assertIsNotNone(y_test)


if __name__ == '__main__':
    unittest.main()

import unittest
from pathlib import Path
import pandas as pd

class TestGTNFileIsValid(unittest.TestCase):

    def setUp(self):
        self.gtn_file = Path("data/pass_cases/GTN.xlsx")

    def test_is_file_excel(self):

        try:
            pd.read_excel(self.gtn_file)

        except Exception as e:
            self.fail(f'File is not a valid Excel file, error type: {e}.')

    def test_no_empty_rows(self):

        df = pd.read_excel(self.gtn_file)

        self.assertEqual(
            len(df), len(df.dropna(how="all")),
            "GTN file contains empty rows."
        )

    def test_header_changes(self):

        df = pd.read_excel(self.gtn_file)

        header = df.columns.to_list()
        expected_header = ["employee_id", "tax_id", "firstname", "lastname", "salary",
 "element1", "element2", "element3", "element4", "element5",
 "element6", "element7", "element8", "element9", "element10"]

        missing_columns = [col for col in expected_header if col not in header]
        self.assertFalse(
            missing_columns,
            f'Missing columns in GTN header: {missing_columns}')

        extra_columns = [col for col in header if col not in expected_header]
        self.assertFalse(
            extra_columns,
            f'Extra columns in GTN header: {extra_columns}')

        if header != expected_header:
            self.fail("Header column order is incorrect.")

        self.assertNotEqual(
            [str(col) for col in df.columns], [str(row) for row in df.iloc[0]],
            "Duplicated headers on second row in GTN file."
        )
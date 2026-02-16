import json
import unittest
from pathlib import Path
import pandas as pd

class TestPayElements(unittest.TestCase):

    def setUp(self):
        self.gtn_file = Path("data/pass_cases/GTN.xlsx")
        self.payrun_file = Path("data/pass_cases/Payrun.xlsx")
        self.mapping_file = Path("data/pass_cases/mapping.json")

        self.gtn_df = pd.read_excel(self.gtn_file)
        self.payrun_df = pd.read_excel(self.payrun_file)

        with open(self.mapping_file) as f:
            self.data = json.load(f)

        self.mapping_payslip_keys = list(self.data["mappings"].keys())
        self.map_gtn_cols = list(self.data["mappings"])
        self.map_payslip_cols = []

        for key in self.mapping_payslip_keys:
            vendor = self.data["mappings"][key]["vendor"]
            self.map_payslip_cols.append(vendor)

        self.gtn_cols = list(self.gtn_df.columns)[4:]

        if "element8" in self.gtn_cols:
            self.gtn_cols.remove('element8')

        self.payrun_cols = list(self.payrun_df.columns)

    def test_gtn_elements_have_mapping(self):
        missing_in_mapping = [col for col in self.gtn_cols if col not in self.map_payslip_cols]
        self.assertFalse(missing_in_mapping, f"GTN elements with no mapping in Payrun: {missing_in_mapping}")

    def test_payrun_elements_have_mapping(self):
        payrun_elements = [col for col in self.payrun_cols if col in self.map_payslip_cols]
        missing_in_mapping = [col for col in payrun_elements if col not in self.gtn_cols]
        self.assertFalse(missing_in_mapping, f"Payrun elements with no mapping in GTN: {missing_in_mapping}")

    def test_numeric_gtn_elements_only(self):
        for col in self.gtn_cols:
            self.assertTrue(pd.api.types.is_numeric_dtype(self.gtn_df[col]), f"Col: {col} in GTN is not numeric")


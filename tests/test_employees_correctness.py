import unittest
from pathlib import Path
import pandas as pd

class TestEmployeesAreNotMissing(unittest.TestCase):

    def setUp(self):
        self.gtn_file = Path("data/pass_cases/GTN.xlsx")
        self.payrun_file = Path("data/pass_cases/Payrun.xlsx")

        gtn_dt = pd.read_excel(self.gtn_file)
        payrun_dt = pd.read_excel(self.payrun_file)

        self.emp_id_list_gtn = gtn_dt['employee_id'].tolist()
        self.emp_id_list_payrun = payrun_dt["Employee ID"].dropna().tolist()
        self.emp_id_list_payrun_in_int = [int(id) for id in self.emp_id_list_payrun]


    def test_gtn_employees_exist_in_payrun(self):
        self.missing_in_gtn = [emp_id for emp_id in self.emp_id_list_gtn if
                               emp_id not in self.emp_id_list_payrun_in_int]

        if self.missing_in_gtn:
            self.assertFalse(f"There are missing employee IDs in GTN file with ID's: {self.missing_in_gtn}")

    def test_payrun_employees_exist_in_gtn(self):
        self.missing_emp_in_payrun = [emp_id for emp_id in self.emp_id_list_payrun_in_int if
                                      emp_id not in self.emp_id_list_gtn]

        if self.missing_emp_in_payrun:
            self.assertFalse(f"There are missing employee IDs in Payrun file with ID's: {self.missing_emp_in_payrun}")

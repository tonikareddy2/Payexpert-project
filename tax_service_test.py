import unittest
from unittest.mock import MagicMock
from DAO.tax_service import TaxService
from Myexceptions.custom_exceptions import (
    InvalidInputException,
    TaxCalculationException,
)


class TestTaxService(unittest.TestCase):
    def setUp(self):
        self.tax_service = TaxService()
        # Mocking the execute method of pyodbc.Cursor
        self.tax_service.cursor.execute = MagicMock()

    def test_read_taxes(self):
        # Mocking the fetchall method to return test data
        self.tax_service.cursor.fetchall.return_value = [(1, 1, 2023, 50000)]
        taxes = self.tax_service.read_taxes()
        self.assertIsNotNone(taxes)
        self.assertEqual(len(taxes), 1)

    def test_calculate_tax(self):
        # Mocking the fetchone method to return test data
        self.tax_service.cursor.fetchone.return_value = (50000,)
        employee_id = 1
        tax_year = 2023
        self.tax_service.calculate_tax(employee_id, tax_year)
        # Add assertions to check if tax is calculated successfully

    def test_calculate_tax_no_taxable_income(self):
        # Mocking the fetchone method to return None
        self.tax_service.cursor.fetchone.return_value = None
        employee_id = 1
        tax_year = 2023
        with self.assertRaises(TaxCalculationException):
            self.tax_service.calculate_tax(employee_id, tax_year)

    def test_calculate_tax_invalid_tax_year(self):
        employee_id = 1
        tax_year = -2023  # Invalid tax year
        with self.assertRaises(InvalidInputException):
            self.tax_service.calculate_tax(employee_id, tax_year)

    def test_get_tax_by_id(self):
        # Mocking the fetchone method to return test data
        self.tax_service.cursor.fetchone.return_value = (1, 1, 2023, 50000)
        tax_id = 1
        tax = self.tax_service.get_tax_by_id(tax_id)
        self.assertIsNotNone(tax)
        # Add more assertions to validate tax data

    def test_get_taxes_for_employee(self):
        # Mocking the fetchall method to return test data
        self.tax_service.cursor.fetchall.return_value = [(1, 1, 2023, 50000)]
        employee_id = 1
        taxes = self.tax_service.get_taxes_for_employee(employee_id)
        self.assertIsNotNone(taxes)
        self.assertEqual(len(taxes), 1)

    def test_get_taxes_for_year(self):
        # Mocking the fetchall method to return test data
        self.tax_service.cursor.fetchall.return_value = [(1, 1, 2023, 50000)]
        tax_year = 2023
        taxes = self.tax_service.get_taxes_for_year(tax_year)
        self.assertIsNotNone(taxes)
        self.assertEqual(len(taxes), 1)


if __name__ == "__main__":
    unittest.main()

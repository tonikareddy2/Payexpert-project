import unittest
from DAO.financialrecord_service import FinancialRecordService
from decimal import Decimal


class TestFinancialRecordServiceModule(unittest.TestCase):
    def setUp(self):
        self.financial_record_service = FinancialRecordService()

    def tearDown(self):
        # Clean up after each test case
        self.financial_record_service = None

    def test_read_financial_records(self):
        records = self.financial_record_service.read_financial_records()
        self.assertIsNotNone(records)

    def test_add_financial_record(self):
        employee_id = 1
        description = "Test expense"
        amount = Decimal("100.0")
        record_type = "Expense"
        self.financial_record_service.add_financial_record(
            employee_id, description, amount, record_type
        )
        # You can add assertions here to check if the record is added successfully.

    def test_get_financial_record_by_id(self):
        record_id = 1
        record = self.financial_record_service.get_financial_record_by_id(record_id)
        self.assertIsNotNone(record)

    def test_get_financial_records_for_employee(self):
        employee_id = 1
        records = self.financial_record_service.get_financial_records_for_employee(
            employee_id
        )
        self.assertIsNotNone(records)

    def test_get_financial_records_for_date(self):
        record_date = "2024-05-01"  # Example date
        records = self.financial_record_service.get_financial_records_for_date(
            record_date
        )
        self.assertIsNotNone(records)


if __name__ == "__main__":
    unittest.main()

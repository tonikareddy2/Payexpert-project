import unittest
from DAO.payroll_service import PayrollService


class TestPayrollServiceModule(unittest.TestCase):
    def setUp(self):
        self.payroll_service = PayrollService()

    def test_read_payrolls(self):
        payrolls = self.payroll_service.read_payrolls()
        self.assertIsNotNone(payrolls)

    def test_generate_payroll(self):
        employee_id = 1
        start_date = "2024-05-01"
        end_date = "2024-05-15"
        self.payroll_service.generate_payroll(employee_id, start_date, end_date)
        # You can add assertions here to validate the generated payroll data.

    def test_get_payroll_by_id(self):
        payroll_id = 1
        payroll = self.payroll_service.get_payroll_by_id(payroll_id)
        self.assertIsNotNone(payroll)

    def test_get_payrolls_for_employee(self):
        employee_id = 1
        payrolls = self.payroll_service.get_payrolls_for_employee(employee_id)
        self.assertIsNotNone(payrolls)

    def test_get_payrolls_for_period(self):
        start_date = "2024-05-01"
        end_date = "2024-05-15"
        payrolls = self.payroll_service.get_payrolls_for_period(start_date, end_date)
        self.assertIsNotNone(payrolls)


if __name__ == "__main__":
    unittest.main()

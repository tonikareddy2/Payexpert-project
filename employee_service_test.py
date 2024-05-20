import unittest
from DAO.employee_service import EmployeeService
from Entity.Employee import Employee


class TestEmployeeServiceModule(unittest.TestCase):
    def setUp(self):
        self.employee_service = EmployeeService()
        # Adding some initial data for testing
        self.test_employee_data = (
            "John",
            "Doe",
            "1990-05-25",
            "M",
            "john.doe@example.com",
            "123456789",
            "123 Main St, City",
            "Manager",
            "2020-01-01",
            "2024-04-20",
        )
        # Create the test employee
        self.test_employee_id = self.employee_service.create_employee(
            self.test_employee_data
        )
        self.assertIsNotNone(self.test_employee_id)

    def tearDown(self):
        # Clean up after each test case
        if self.test_employee_id:
            self.employee_service.delete_employee(self.test_employee_id)
            self.test_employee_id = None

    def test_read_employees(self):
        employees = self.employee_service.read_employees()
        self.assertIsNotNone(employees)
        self.assertGreater(len(employees), 0)

    def test_update_employee(self):
        updated_employee_data = (
            "Updated John",
            "Updated Doe",
            "1990-05-25",
            "M",
            "updated.john.doe@example.com",
            "987654321",
            "123 Main St, City",
            "Manager",
            "2020-01-01",
            "2024-04-20",
        )
        self.employee_service.update_employee(
            updated_employee_data, self.test_employee_id
        )
        updated_employee = self.employee_service.cursor.execute(
            "SELECT * FROM Employee WHERE EmployeeID = ?", (self.test_employee_id,)
        ).fetchone()

        self.assertEqual(updated_employee[1], "Updated John")
        self.assertEqual(updated_employee[2], "Updated Doe")
        self.assertEqual(updated_employee[4], "M")

    def test_delete_employee(self):
        self.employee_service.delete_employee(self.test_employee_id)

        # Check if the employee is deleted
        deleted_employee = self.employee_service.cursor.execute(
            "SELECT * FROM Employee WHERE EmployeeID = ?", (self.test_employee_id,)
        ).fetchone()

        self.assertIsNone(deleted_employee)


if __name__ == "__main__":
    unittest.main()

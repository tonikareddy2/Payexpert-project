class EmployeeNotFoundException(Exception):
    def __init__(self, employee_id):
        super().__init__(f"Employee with ID {employee_id} is not found")


class PayrollGenerationException(Exception):
    def __init__(self):
        super().__init__("PayrollGeneration error occured")


class TaxCalculationException(Exception):
    def __init__(self):
        super().__init__("TaxCalculation error occured")


class FinancialRecordException(Exception):
    def __init__(self):
        super().__init__("Financial record error occured")


class InvalidInputException(Exception):
    def __init__(self):
        super().__init__("Invalid input try again")


class DatabaseConnectionException(Exception):
    def __init__(self):
        super().__init__("Database is not connected correctly, try again")

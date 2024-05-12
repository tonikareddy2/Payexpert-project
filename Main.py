import pyodbc

server_name = "DESKTOP-P8QAI2N\SQLEXPRESS"
database_name = "payXpert"


conn_str = (
    f"Driver={{SQL Server}};"
    f"Server={server_name};"
    f"Database={database_name};"
    f"Trusted_Connection=yes;"
)
# print(conn_str)
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()
cursor.execute("SELECT 1")
print("Database connection is successful")


class EmployeeService:

    def read_employees(self):
        cursor.execute("SELECT * FROM Employee")
        employees = cursor.fetchall()
        for employee in employees:
            print(employee)

    def create_employee(self, employee_data):
        cursor.execute(
            "INSERT INTO Employee (FirstName, LastName, DateOfBirth, Gender, Email, PhoneNumber, Address, Position, JoiningDate, TerminationDate) VALUES(?,?,?,?,?,?,?,?,?,?)",
            employee_data,
        )
        conn.commit()
        print("Employee inserted successfully.")

    def delete_employee(self, employee_id):
        cursor.execute("DELETE FROM Employee WHERE EmployeeID = ?", (employee_id,))
        conn.commit()
        print("Employee deleted successfully.")

    def update_employee(self, employee_data):
        cursor.execute(
            """
            UPDATE Employee
            SET FirstName = ?, LastName = ?, DateOfBirth = ?, Gender = ?, Email = ?, PhoneNumber = ?, Address = ?, Position = ?, JoiningDate = ?, TerminationDate = ?
            WHERE EmployeeID = ?
            """,
            employee_data,
        )
        conn.commit()
        print("Employee updated successfully.")


class PayrollService:

    def read_payrolls(self):
        cursor.execute("SELECT * FROM Payroll")
        payrolls = cursor.fetchall()
        for payroll in payrolls:
            print(payroll)

    def generate_payroll(self, employee_id, start_date, end_date):
        # Your logic for generating payroll goes here
        pass

    def get_payroll_by_id(self, payroll_id):
        cursor.execute("SELECT * FROM Payroll WHERE PayrollID = ?", (payroll_id,))
        payroll = cursor.fetchone()
        print(payroll)

    def get_payrolls_for_employee(self, employee_id):
        cursor.execute("SELECT * FROM Payroll WHERE EmployeeID = ?", (employee_id,))
        payrolls = cursor.fetchall()
        for payroll in payrolls:
            print(payroll)

    def get_payrolls_for_period(self, start_date, end_date):
        cursor.execute(
            "SELECT * FROM Payroll WHERE PayPeriodStartDate >= ? AND PayPeriodEndDate <= ?",
            (start_date, end_date),
        )
        payrolls = cursor.fetchall()
        for payroll in payrolls:
            print(payroll)


class TaxService:

    def read_taxes(self):
        cursor.execute("SELECT * FROM Tax")
        taxes = cursor.fetchall()
        for tax in taxes:
            print(tax)

    def calculate_tax(self, employee_id, tax_year):
        # Your logic for calculating taxes goes here
        pass

    def get_tax_by_id(self, tax_id):
        cursor.execute("SELECT * FROM Tax WHERE TaxID = ?", (tax_id,))
        tax = cursor.fetchone()
        print(tax)

    def get_taxes_for_employee(self, employee_id):
        cursor.execute("SELECT * FROM Tax WHERE EmployeeID = ?", (employee_id,))
        taxes = cursor.fetchall()
        for tax in taxes:
            print(tax)

    def get_taxes_for_year(self, tax_year):
        cursor.execute("SELECT * FROM Tax WHERE TaxYear = ?", (tax_year,))
        taxes = cursor.fetchall()
        for tax in taxes:
            print(tax)


class FinancialRecordService:

    def read_financial_records(self):
        cursor.execute("SELECT * FROM FinancialRecord")
        records = cursor.fetchall()
        for record in records:
            print(record)

    def add_financial_record(self, employee_id, description, amount, record_type):
        cursor.execute(
            "INSERT INTO FinancialRecord (EmployeeID, RecordDate, Description, Amount, RecordType) VALUES (?,?,?,?,?)",
            (employee_id, datetime.now(), description, amount, record_type),
        )
        conn.commit()
        print("Financial record added successfully.")

    def get_financial_record_by_id(self, record_id):
        cursor.execute("SELECT * FROM FinancialRecord WHERE RecordID = ?", (record_id,))
        record = cursor.fetchone()
        print(record)

    def get_financial_records_for_employee(self, employee_id):
        cursor.execute(
            "SELECT * FROM FinancialRecord WHERE EmployeeID = ?", (employee_id,)
        )
        records = cursor.fetchall()
        for record in records:
            print(record)

    def get_financial_records_for_date(self, record_date):
        cursor.execute(
            "SELECT * FROM FinancialRecord WHERE RecordDate = ?", (record_date,)
        )
        records = cursor.fetchall()
        for record in records:
            print(record)


def employee_management():
    employee_service = EmployeeService()

    while True:
        print("1. Create an employee")
        print("2. Delete an employee")
        print("3. Read employees")
        print("4. Update an employee")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            employee_data = (
                input("Enter first name: "),
                input("Enter last name: "),
                input("Enter date of birth (YYYY-MM-DD): "),
                input("Enter gender: "),
                input("Enter email: "),
                input("Enter phone number: "),
                input("Enter address: "),
                input("Enter position: "),
                input("Enter joining date (YYYY-MM-DD): "),
                input("Enter termination date (YYYY-MM-DD, if any): "),
            )
            employee_service.create_employee(employee_data)
        elif choice == "2":
            employee_service.read_employees()
            employee_id = input("Enter the EmployeeID: ")
            employee_service.delete_employee(employee_id)
        elif choice == "3":
            employee_service.read_employees()
        elif choice == "4":
            employee_service.read_employees()
            employee_data = (
                input("Enter first name: "),
                input("Enter last name: "),
                input("Enter date of birth (YYYY-MM-DD): "),
                input("Enter gender: "),
                input("Enter email: "),
                input("Enter phone number: "),
                input("Enter address: "),
                input("Enter position: "),
                input("Enter joining date (YYYY-MM-DD): "),
                input("Enter termination date (YYYY-MM-DD, if any): "),
                input("Enter the EmployeeID to update: "),
            )
            employee_service.update_employee(employee_data)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please enter a valid option.")


employee_management()


def payroll_management():
    payroll_service = PayrollService()

    while True:
        print("1. Generate payroll for an employee")
        print("2. Get payroll by ID")
        print("3. Get payrolls for an employee")
        print("4. Get payrolls for a period")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            employee_id = input("Enter EmployeeID: ")
            start_date = input("Enter Pay Period Start Date (YYYY-MM-DD): ")
            end_date = input("Enter Pay Period End Date (YYYY-MM-DD): ")
            payroll_service.generate_payroll(employee_id, start_date, end_date)
        elif choice == "2":
            payroll_id = input("Enter PayrollID: ")
            payroll_service.get_payroll_by_id(payroll_id)
        elif choice == "3":
            employee_id = input("Enter EmployeeID: ")
            payroll_service.get_payrolls_for_employee(employee_id)
        elif choice == "4":
            start_date = input("Enter Start Date (YYYY-MM-DD): ")
            end_date = input("Enter End Date (YYYY-MM-DD): ")
            payroll_service.get_payrolls_for_period(start_date, end_date)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please enter a valid option.")


payroll_management()


def tax_management():
    tax_service = TaxService()

    while True:
        print("1. Calculate tax for an employee")
        print("2. Get tax by ID")
        print("3. Get taxes for an employee")
        print("4. Get taxes for a year")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            employee_id = input("Enter EmployeeID: ")
            tax_year = input("Enter Tax Year: ")
            tax_service.calculate_tax(employee_id, tax_year)
        elif choice == "2":
            tax_id = input("Enter TaxID: ")
            tax_service.get_tax_by_id(tax_id)
        elif choice == "3":
            employee_id = input("Enter EmployeeID: ")
            tax_service.get_taxes_for_employee(employee_id)
        elif choice == "4":
            tax_year = input("Enter Tax Year: ")
            tax_service.get_taxes_for_year(tax_year)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please enter a valid option.")


tax_management()


def financial_record_management():
    financial_record_service = FinancialRecordService()

    while True:
        print("1. Add a financial record for an employee")
        print("2. Get financial record by ID")
        print("3. Get financial records for an employee")
        print("4. Get financial records for a date")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            employee_id = input("Enter EmployeeID: ")
            description = input("Enter description: ")
            amount = input("Enter amount: ")
            record_type = input("Enter record type: ")
            financial_record_service.add_financial_record(
                employee_id, description, amount, record_type
            )
        elif choice == "2":
            record_id = input("Enter RecordID: ")
            financial_record_service.get_financial_record_by_id(record_id)
        elif choice == "3":
            employee_id = input("Enter EmployeeID: ")
            financial_record_service.get_financial_records_for_employee(employee_id)
        elif choice == "4":
            record_date = input("Enter Record Date (YYYY-MM-DD): ")
            financial_record_service.get_financial_records_for_date(record_date)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please enter a valid option.")


financial_record_management()


class MainMenu:

    @staticmethod
    def main_menu():
        while True:
            print("Main Menu:")
            print("1. Employee Management")
            print("2. Payroll Management")
            print("3. Tax Management")
            print("4. Financial Record Management")
            print("5. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                employee_management()
            elif choice == "2":
                payroll_management()
            elif choice == "3":
                tax_management()
            elif choice == "4":
                financial_record_management()
            elif choice == "5":
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    MainMenu.main_menu()

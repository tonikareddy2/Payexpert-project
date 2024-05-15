import pyodbc
from DAO import EmployeeService, FinancialRecordService, TaxService, PayrollService
from Entity import Employee, FinancialRecord, Tax, Payroll


class MainMenu:
    employee_service = EmployeeService()
    financialrecord_service = FinancialRecordService()
    payroll_service = PayrollService()
    tax_service = TaxService()

    def employee_management(self):
        while True:
            print(
                """1. Create an employee
                   2. Delete an employee
                   3. Read employees
                   4. Update an employee
                   5. Back to Main Menu
            """
            )
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
                self.employee_service.create_employee(employee_data)
            elif choice == "2":
                self.employee_service.read_employees()
                employee_id = input("Enter the EmployeeID: ")
                self.employee_service.delete_employee(employee_id)
            elif choice == "3":
                self.employee_service.read_employees()
            elif choice == "4":
                self.employee_service.read_employees()
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
                self.employee_service.update_employee(employee_data)
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please enter a valid option.")

    def payroll_management(self):
        while True:
            print(
                """1. Generate payroll for an employee
                   2. Get payroll by ID
                   3. Get payrolls for an employee
                   4. Get payrolls for a period
                   5. Back to Main Menu
            """
            )
            choice = input("Enter your choice: ")

            if choice == "1":
                employee_id = input("Enter EmployeeID: ")
                start_date = input("Enter Pay Period Start Date (YYYY-MM-DD): ")
                end_date = input("Enter Pay Period End Date (YYYY-MM-DD): ")
                self.payroll_service.generate_payroll(employee_id, start_date, end_date)
            elif choice == "2":
                payroll_id = input("Enter PayrollID: ")
                self.payroll_service.get_payroll_by_id(payroll_id)
            elif choice == "3":
                employee_id = input("Enter EmployeeID: ")
                self.payroll_service.get_payrolls_for_employee(employee_id)
            elif choice == "4":
                start_date = input("Enter Start Date (YYYY-MM-DD): ")
                end_date = input("Enter End Date (YYYY-MM-DD): ")
                self.payroll_service.get_payrolls_for_period(start_date, end_date)
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please enter a valid option.")

    def tax_management(self):

        while True:
            print(
                """1. Calculate tax for an employee
                   2. Get tax by ID
                   3. Get taxes for an employee
                   4. Get taxes for a year
                   5. Back to Main Menu
                   """
            )
            choice = input("Enter your choice: ")

            if choice == "1":
                employee_id = input("Enter EmployeeID: ")
                tax_year = input("Enter Tax Year: ")
                self.tax_service.calculate_tax(employee_id, tax_year)
            elif choice == "2":
                tax_id = input("Enter TaxID: ")
                self.tax_service.get_tax_by_id(tax_id)
            elif choice == "3":
                employee_id = input("Enter EmployeeID: ")
                self.tax_service.get_taxes_for_employee(employee_id)
            elif choice == "4":
                tax_year = input("Enter Tax Year: ")
                self.tax_service.get_taxes_for_year(tax_year)
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please enter a valid option.")

    def financial_record_management(self):
        while True:
            print(
                """1. Add a financial record for an employee
                   2. Get financial record by ID
                   3. Get financial records for an employee
                   4. Get financial records for a date
                   5. Back to Main Menu"""
            )
            choice = input("Enter your choice: ")

            if choice == "1":
                employee_id = input("Enter EmployeeID: ")
                description = input("Enter description: ")
                amount = input("Enter amount: ")
                record_type = input("Enter record type: ")
                self.financial_record_service.add_financial_record(
                    employee_id, description, amount, record_type
                )
            elif choice == "2":
                record_id = input("Enter RecordID: ")
                self.financialrecord_service.get_financial_record_by_id(record_id)
            elif choice == "3":
                employee_id = input("Enter EmployeeID: ")
                self.financialrecord_service.get_financial_records_for_employee(
                    employee_id
                )
            elif choice == "4":
                record_date = input("Enter Record Date (YYYY-MM-DD): ")
                self.financialrecord_service.get_financial_records_for_date(record_date)
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please enter a valid option.")


def main():
    main_menu = MainMenu()
    while True:
        print(
            """Main Menu:
            1. Employee Management
            2. Payroll Management
            3. Tax Management
            4. Financial Record Management
            5. Exit"""
        )
        choice = input("Enter your choice: ")

        if choice == "1":
            main_menu.employee_management()
        elif choice == "2":
            main_menu.payroll_management()
        elif choice == "3":
            main_menu.tax_management()
        elif choice == "4":
            main_menu.financial_record_management()
        elif choice == "5":
            print("Goodbye! Come back soon")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    print("Welcome to payroll management system")
    main()

from Util.DBconn import DBconnection
from Entity import Tax
from Myexceptions.custom_exceptions import (
    InvalidInputException,
    TaxCalculationException,
)
from decimal import Decimal
from abc import ABC, abstractmethod


class ITaxService(ABC):
    @abstractmethod
    def read_taxes(self):
        pass

    @abstractmethod
    def calculate_tax(self, employee_id, tax_year):
        pass

    @abstractmethod
    def get_tax_by_id(self, tax_id):
        pass

    @abstractmethod
    def get_taxes_for_employee(self, employee_id):
        pass

    @abstractmethod
    def get_taxes_for_year(self, tax_year):
        pass


class TaxService(ITaxService, DBconnection):

    def read_taxes(self):
        try:
            self.cursor.execute("SELECT * FROM Tax")
            taxes = self.cursor.fetchall()
            for tax in taxes:
                print(tax)
        except Exception as e:
            print(e)

    def calculate_tax(self, employee_id, tax_year):
        try:
            # Validate the tax year
            if not tax_year.isdigit() or int(tax_year) < 0:
                raise InvalidInputException("Invalid tax year entered.")

            # Validate employee_id
            if not employee_id.isdigit() or int(employee_id) <= 0:
                raise InvalidInputException("Invalid Employee ID entered.")

            employee_id = int(employee_id)
            tax_year = int(tax_year)

            # Fetch taxable income
            self.cursor.execute(
                "SELECT SUM(TaxableIncome) FROM Tax WHERE EmployeeID = ? AND TaxYear = ?",
                (employee_id, tax_year),
            )
            total_taxable_income = self.cursor.fetchone()[0]

            if total_taxable_income is None:
                raise TaxCalculationException(
                    f"No taxable income found for Employee ID {employee_id} in Tax Year {tax_year}"
                )

            # Convert the total taxable income to Decimal if it's not already
            if not isinstance(total_taxable_income, Decimal):
                total_taxable_income = Decimal(total_taxable_income)

            # Apply tax rate
            tax_rate = Decimal("0.15")  # Use Decimal for the tax rate
            tax_amount = total_taxable_income * tax_rate

            tax = Tax(None, employee_id, tax_year, total_taxable_income, tax_amount)

            print(
                f"Tax calculated for Employee ID {tax.EmployeeID} for Tax Year {tax.TaxYear}:"
            )
            print(f"Total Taxable Income: {tax.TaxableIncome}")
            print(f"Tax Rate: {tax_rate}")
            print(f"Tax Amount: {tax.TaxAmount}")

        except InvalidInputException as iie:
            print(f"Input Error: {iie}")
        except TaxCalculationException as tce:
            print(f"Calculation Error: {tce}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def get_tax_by_id(self, tax_id):
        try:
            self.cursor.execute("SELECT * FROM Tax WHERE TaxID = ?", (tax_id,))
            tax = self.cursor.fetchone()
            print(tax)
        except Exception as e:
            print(e)

    def get_taxes_for_employee(self, employee_id):
        try:
            self.cursor.execute(
                "SELECT * FROM Tax WHERE EmployeeID = ?", (employee_id,)
            )
            taxes = self.cursor.fetchall()
            for tax in taxes:
                print(tax)
        except Exception as e:
            print(e)

    def get_taxes_for_year(self, tax_year):
        try:
            self.cursor.execute("SELECT * FROM Tax WHERE TaxYear = ?", (tax_year,))
            taxes = self.cursor.fetchall()
            for tax in taxes:
                print(tax)
        except Exception as e:
            print(e)

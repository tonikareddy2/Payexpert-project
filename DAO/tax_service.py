from Util.DBconn import DBconnection
from Myexceptions.custom_exceptions import (
    InvalidInputException,
    TaxCalculationException,
)
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


class TaxService(ITaxService,DBconnection):

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
            self.cursor.execute(
                "SELECT SUM(TaxableIncome) FROM Tax WHERE EmployeeID = ? AND TaxYear = ?",
                (employee_id, tax_year),
            )
            total_taxable_income = self.cursor.fetchone()[0]
            if total_taxable_income is None:
                raise TaxCalculationException(
                    f"No taxable income found for Employee ID {employee_id} in Tax Year {tax_year}"
                )
            if tax_year < 0:  # Example condition for invalid tax year
                raise InvalidInputException("Tax year cannot be negative")
            # Applying tax rate (assuming a fixed tax rate for simplicity)
            tax_rate = 0.15
            tax_amount = total_taxable_income * tax_rate
            print(
                f"Tax calculated for Employee ID {employee_id} for Tax Year {tax_year}:"
            )
            print(f"Total Taxable Income: {total_taxable_income}")
            print(f"Tax Rate: {tax_rate}")
            print(f"Tax Amount: {tax_amount}")
        except Exception as e:
            print(e)

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

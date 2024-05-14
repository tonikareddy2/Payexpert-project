class TaxService:

    def read_taxes(self):
        self.cursor.execute("SELECT * FROM Tax")
        taxes = self.cursor.fetchall()
        for tax in taxes:
            print(tax)

    def calculate_tax(self, employee_id, tax_year):
        # Your logic for calculating taxes goes here
        pass

    def get_tax_by_id(self, tax_id):
        self.cursor.execute("SELECT * FROM Tax WHERE TaxID = ?", (tax_id,))
        tax = self.cursor.fetchone()
        print(tax)

    def get_taxes_for_employee(self, employee_id):
        self.cursor.execute("SELECT * FROM Tax WHERE EmployeeID = ?", (employee_id,))
        taxes = self.cursor.fetchall()
        for tax in taxes:
            print(tax)

    def get_taxes_for_year(self, tax_year):
        self.cursor.execute("SELECT * FROM Tax WHERE TaxYear = ?", (tax_year,))
        taxes = self.cursor.fetchall()
        for tax in taxes:
            print(tax)

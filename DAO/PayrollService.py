class PayrollService:

    def read_payrolls(self):
        self.cursor.execute("SELECT * FROM Payroll")
        payrolls = self.cursor.fetchall()
        for payroll in payrolls:
            print(payroll)

    def generate_payroll(self, employee_id, start_date, end_date):
        # Your logic for generating payroll goes here
        pass

    def get_payroll_by_id(self, payroll_id):
        self.cursor.execute("SELECT * FROM Payroll WHERE PayrollID = ?", (payroll_id,))
        payroll = self.cursor.fetchone()
        print(payroll)

    def get_payrolls_for_employee(self, employee_id):
        self.cursor.execute(
            "SELECT * FROM Payroll WHERE EmployeeID = ?", (employee_id,)
        )
        payrolls = self.cursor.fetchall()
        for payroll in payrolls:
            print(payroll)

    def get_payrolls_for_period(self, start_date, end_date):
        self.cursor.execute(
            "SELECT * FROM Payroll WHERE PayPeriodStartDate >= ? AND PayPeriodEndDate <= ?",
            (start_date, end_date),
        )
        payrolls = self.cursor.fetchall()
        for payroll in payrolls:
            print(payroll)

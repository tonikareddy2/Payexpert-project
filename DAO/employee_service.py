class EmployeeService:

    def read_employees(self):
        self.cursor.execute("SELECT * FROM Employee")
        employees = self.cursor.fetchall()
        for employee in employees:
            print(employee)

    def create_employee(self, employee_data):
        self.cursor.execute(
            "INSERT INTO Employee (FirstName, LastName, DateOfBirth, Gender, Email, PhoneNumber, Address, Position, JoiningDate, TerminationDate) VALUES(?,?,?,?,?,?,?,?,?,?)",
            employee_data,
        )
        self.conn.commit()
        print("Employee inserted successfully.")

    def delete_employee(self, employee_id):
        self.cursor.execute("DELETE FROM Employee WHERE EmployeeID = ?", (employee_id,))
        self.conn.commit()
        print("Employee deleted successfully.")

    def update_employee(self, employee_data):
        self.cursor.execute(
            """
            UPDATE Employee
            SET FirstName = ?, LastName = ?, DateOfBirth = ?, Gender = ?, Email = ?, PhoneNumber = ?, Address = ?, Position = ?, JoiningDate = ?, TerminationDate = ?
            WHERE EmployeeID = ?
            """,
            employee_data,
        )
        self.conn.commit()
        print("Employee updated successfully.")

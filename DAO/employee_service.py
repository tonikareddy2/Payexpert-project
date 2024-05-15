from Util.DBconn import DBconnection
from Myexceptions.custom_exceptions import EmployeeNotFoundException


class EmployeeService(DBconnection):

    def read_employees(self):
        try:
            self.cursor.execute("SELECT * FROM Employee")
            employees = self.cursor.fetchall()
            for employee in employees:
                print(employee)
        except Exception as e:
            print(e)

    def create_employee(self, employee_data):
        try:
            self.cursor.execute(
                "INSERT INTO Employee (FirstName, LastName, DateOfBirth, Gender, Email, PhoneNumber, Address, Position, JoiningDate, TerminationDate) VALUES(?,?,?,?,?,?,?,?,?,?)",
                employee_data,
            )
            self.conn.commit()
            print("Employee inserted successfully.")
        except Exception as e:
            print(e)

    def delete_employee(self, employee_id):
        try:
            self.cursor.execute(
                "DELETE FROM Employee WHERE EmployeeID = ?", (employee_id,)
            )
            if self.cursor.rowcount == 0:
                raise EmployeeNotFoundException(employee_id)
            self.conn.commit()
            print("Employee deleted successfully.")
        except Exception as e:
            print(e)

    def update_employee(self, employee_data):
        try:
            self.cursor.execute(
                """
                UPDATE Employee
                SET FirstName = ?, LastName = ?, DateOfBirth = ?, Gender = ?, Email = ?, PhoneNumber = ?, Address = ?, Position = ?, JoiningDate = ?, TerminationDate = ?
                WHERE EmployeeID = ?
                """,
                employee_data,
            )
            if self.cursor.rowcount == 0:
                raise EmployeeNotFoundException(employee_data[10])
            self.conn.commit()
            print("Employee updated successfully.")
        except Exception as e:
            print(e)

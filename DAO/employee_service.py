from Util.DBconn import DBconnection
from Myexceptions.custom_exceptions import EmployeeNotFoundException
from abc import ABC, abstractmethod


class IEmployeeService(ABC):
    @abstractmethod
    def read_employees(self):
        pass

    @abstractmethod
    def create_employee(self, employee_data):
        pass

    @abstractmethod
    def update_employee(self, employee_data, employee_id):
        pass

    @abstractmethod
    def delete_employee(self, employee_id):
        pass


class EmployeeService(DBconnection, IEmployeeService):

    def read_employees(self):
        try:
            self.cursor.execute("SELECT * FROM Employee")
            employees = self.cursor.fetchall()
            for employee in employees:
                print(employee)
            return employees
        except Exception as e:
            print(e)

    def create_employee(self, employee_data):
        try:
            self.cursor.execute("SELECT MAX(EmployeeID) FROM Employee")
            max_employee_id = self.cursor.fetchone()[0]
            next_employee_id = max_employee_id + 1 if max_employee_id else 1
            employee_data_with_id = (
                (next_employee_id,)
                + tuple(employee_data[:4])
                + (employee_data[3],)  # Corrected index for gender
                + tuple(employee_data[5:])
            )
            self.cursor.execute(
                """
                INSERT INTO Employee (EmployeeID, FirstName, LastName, DateOfBirth, Gender, Email, PhoneNumber, Address, Position, JoiningDate, TerminationDate) 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                employee_data_with_id,
            )
            self.conn.commit()
            return next_employee_id  # Return the newly generated employee ID
        except Exception as e:
            print(e)
            return None

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

    def update_employee(self, employee_data, employee_id):
        try:
            self.cursor.execute(
                """
                UPDATE Employee
                SET FirstName = ?, LastName = ?, DateOfBirth = ?, Gender = ?, Email = ?, PhoneNumber = ?, Address = ?, Position = ?, JoiningDate = ?, TerminationDate = ?
                WHERE EmployeeID = ?
                """,
                (
                    employee_data[0],  # FirstName
                    employee_data[1],  # LastName
                    employee_data[2],  # DateOfBirth
                    employee_data[3],  # Gender
                    employee_data[4],  # Email
                    employee_data[5],  # PhoneNumber
                    employee_data[6],  # Address
                    employee_data[7],  # Position
                    employee_data[8],  # JoiningDate
                    employee_data[9],  # TerminationDate
                    employee_id,  # EmployeeID
                ),
            )
            if self.cursor.rowcount == 0:
                raise EmployeeNotFoundException(employee_id)
            self.conn.commit()
            print("Employee updated successfully.")
        except Exception as e:
            print(e)

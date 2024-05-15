from datetime import datetime
from Util.DBconn import DBconnection


class FinancialRecordService(DBconnection):

    def read_financial_records(self):
        try:
            self.cursor.execute("SELECT * FROM FinancialRecord")
            records = self.cursor.fetchall()
            for record in records:
                print(record)
        except Exception as e:
            print(e)

    def add_financial_record(self, employee_id, description, amount, record_type):
        try:
            self.cursor.execute(
                "INSERT INTO FinancialRecord (EmployeeID, RecordDate, Description, Amount, RecordType) VALUES (?,?,?,?,?)",
                (employee_id, datetime.now(), description, amount, record_type),
            )
            self.conn.commit()
            print("Financial record added successfully.")
        except Exception as e:
            print(e)

    def get_financial_record_by_id(self, record_id):
        try:
            self.cursor.execute(
                "SELECT * FROM FinancialRecord WHERE RecordID = ?", (record_id,)
            )
            record = self.cursor.fetchone()
            print(record)
        except Exception as e:
            print(e)

    def get_financial_records_for_employee(self, employee_id):
        try:
            self.cursor.execute(
                "SELECT * FROM FinancialRecord WHERE EmployeeID = ?", (employee_id,)
            )
            records = self.cursor.fetchall()
            for record in records:
                print(record)
        except Exception as e:
            print(e)

    def get_financial_records_for_date(self, record_date):
        try:
            self.cursor.execute(
                "SELECT * FROM FinancialRecord WHERE RecordDate = ?", (record_date,)
            )
            records = self.cursor.fetchall()
            for record in records:
                print(record)
        except Exception as e:
            print(e)

from datetime import datetime
from decimal import Decimal
from Util.DBconn import DBconnection
from Entity import FinancialRecord
from Myexceptions.custom_exceptions import FinancialRecordException
from abc import ABC, abstractmethod


class IFinancialRecordService(ABC):
    @abstractmethod
    def read_financial_records(self):
        pass

    @abstractmethod
    def add_financial_record(self, employee_id, description, amount, record_type):
        pass

    @abstractmethod
    def get_financial_record_by_id(self, record_id):
        pass

    @abstractmethod
    def get_financial_records_for_employee(self, employee_id):
        pass

    @abstractmethod
    def get_financial_records_for_date(self, record_date):
        pass


class FinancialRecordService(IFinancialRecordService, DBconnection):

    def read_financial_records(self):
        try:
            self.cursor.execute("SELECT * FROM FinancialRecord")
            records = self.cursor.fetchall()
            for record in records:
                print(record)
            return records
        except Exception as e:
            print(e)

    def add_financial_record(
        self, Record_id, employee_id, RecordDate, description, amount, record_type
    ):
        try:
            self.cursor.execute(
                """
            INSERT INTO FinancialRecord (RecordID, EmployeeID, RecordDate, Description, Amount, RecordType) 
            VALUES (?, ?, ?, ?, ?, ?)

            """,
                (
                    Record_id,
                    employee_id,
                    RecordDate,
                    description,
                    amount,
                    record_type,
                ),
            )
            self.conn.commit()
            print("Financial record added successfully.")
            return True
        except Exception as e:
            print(e)
            return False

    def get_financial_record_by_id(self, record_id):
        try:
            self.cursor.execute(
                "SELECT * FROM FinancialRecord WHERE RecordID = ?", (record_id,)
            )
            record = self.cursor.fetchone()
            print(record)
            return record
        except Exception as e:
            print(e)

    def get_financial_records_for_employee(self, employee_id):
        try:
            self.cursor.execute(
                "SELECT * FROM FinancialRecord WHERE EmployeeID = ?", (employee_id,)
            )
            records = self.cursor.fetchall()
            if not records:
                raise FinancialRecordException(
                    f"No financial records found for Employee ID {employee_id}."
                )
            for record in records:
                print(record)
            return records
        except Exception as e:
            print(e)

    def get_financial_records_for_date(self, record_date):
        try:
            self.cursor.execute(
                "SELECT * FROM FinancialRecord WHERE CONVERT(date, RecordDate) = ?",
                (record_date,),
            )
            records = self.cursor.fetchall()
            if not records:
                raise FinancialRecordException(record_date)
            for record in records:
                print(record)
            return records
        except FinancialRecordException as e:
            print(e)
        except Exception as e:
            print(e)

-- Insert sample records into Employee table
INSERT INTO Employee (EmployeeID, FirstName, LastName, DateOfBirth, Gender, Email, PhoneNumber, Address, Position, JoiningDate, TerminationDate) 
VALUES 
    (1, 'John', 'Doe', '1985-05-15', 'M', 'john@example.com', '1234567890', '123 Main St', 'Developer', '2020-01-01', NULL),
    (2, 'Jane', 'Smith', '1990-08-25', 'F', 'jane@example.com', '9876543210', '456 Elm St', 'Manager', '2019-07-15', NULL),
    (3, 'Michael', 'Johnson', '1982-03-10', 'M', 'michael@example.com', '5555555555', '789 Oak St', 'Sales Associate', '2021-02-20', NULL),
    (4, 'Emily', 'Brown', '1995-11-20', 'F', 'emily@example.com', '2223334444', '101 Pine St', 'HR Coordinator', '2018-09-10', NULL),
    (5, 'David', 'Wilson', '1988-07-03', 'M', 'david@example.com', '7778889999', '321 Cedar St', 'Accountant', '2022-04-05', NULL);

-- Insert sample records into Payroll table
INSERT INTO Payroll (PayrollID, EmployeeID, PayPeriodStartDate, PayPeriodEndDate, BasicSalary, OvertimePay, Deductions, NetSalary) 
VALUES 
    (1, 1, '2024-05-01', '2024-05-15', 5000.00, 200.00, 300.00, 4700.00),
    (2, 2, '2024-05-01', '2024-05-15', 6000.00, 300.00, 400.00, 5700.00),
    (3, 3, '2024-05-01', '2024-05-15', 5500.00, 250.00, 350.00, 5400.00),
    (4, 4, '2024-05-01', '2024-05-15', 5200.00, 220.00, 320.00, 5100.00),
    (5, 5, '2024-05-01', '2024-05-15', 5800.00, 280.00, 380.00, 5700.00);

-- Insert sample records into Tax table
INSERT INTO Tax (TaxID, EmployeeID, TaxYear, TaxableIncome, TaxAmount) 
VALUES 
    (1, 1, 2024, 55000.00, 8000.00),
    (2, 2, 2024, 60000.00, 8500.00),
    (3, 3, 2024, 58000.00, 8200.00),
    (4, 4, 2024, 53000.00, 7800.00),
    (5, 5, 2024, 62000.00, 8800.00);

-- Insert sample records into FinancialRecord table
INSERT INTO FinancialRecord (RecordID, EmployeeID, RecordDate, Description, Amount, RecordType) 
VALUES 
    (1, 1, '2024-05-01', 'Bonus', 1000.00, 'Income'),
    (2, 2, '2024-05-01', 'Travel Expenses', 500.00, 'Expense'),
    (3, 3, '2024-05-01', 'Commission', 700.00, 'Income'),
    (4, 4, '2024-05-01', 'Training Course Fee', 300.00, 'Expense'),
    (5, 5, '2024-05-01', 'Salary', 5800.00, 'Income');

SELECT * FROM Employee;
SELECT * FROM FinancialRecord;
SELECT * FROM Payroll;
SELECT * FROM Tax;
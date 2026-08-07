# Employee Payroll Management System

A Command Line Interface (CLI) based Employee Payroll Management System developed using **Python** and **MySQL**. This project allows users to manage employee records, perform CRUD operations, calculate salaries, and retrieve employee information efficiently through a simple menu-driven interface.

---

## Features

- ➕ Add Employee
- 📋 View All Employees
- 🔍 Search Employee by ID
- ✏️ Update Employee Details
- ❌ Delete Employee
- 💰 Calculate Employee Salary (Bonus, Tax & Net Salary)
- 🏆 Display Highest Paid Employee
- 🏢 View Department-wise Employees
- 🗄️ MySQL Database Integration
- ⚠️ Exception Handling for Duplicate Employee IDs

---

## Technologies Used

- Python 3
- MySQL
- mysql-connector-python
- Object-Oriented Programming (OOP)

---

## Project Structure

```
Employee_Payroll_Management_System/
│
├── Employee_payroll_management.py
├── Employee_payroll_mysql.py
├── employee_payroll.sql
├── requirements.txt
├── .gitignore
├── README.md
└── config.py (Not uploaded to GitHub)
```

---

## Database Schema

```sql
CREATE DATABASE employee_payroll;

USE employee_payroll;

CREATE TABLE employee (
    employee_id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT NOT NULL,
    dept VARCHAR(50),
    designation VARCHAR(50),
    salary FLOAT
);
```

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Employee_Payroll_Management_System.git
```

### 2. Navigate to the Project Folder

```bash
cd Employee_Payroll_Management_System
```

### 3. Install Required Package

```bash
pip install -r requirements.txt
```

### 4. Create the Database

Open **MySQL Workbench** and execute the SQL script:

```sql
employee_payroll.sql
```

### 5. Configure Database Credentials

Update your database credentials inside **config.py** or your database connection file.

Example:

```python
host = "localhost"
user = "root"
password = "YOUR_PASSWORD"
database = "employee_payroll"
```

### 6. Run the Project

```bash
python Employee_payroll_mysql.py
```

---

## Menu Options

```
1. Add Employee
2. View Employees
3. Search Employee
4. Update Employee
5. Delete Employee
6. Calculate Salary
7. Highest Paid Employee
8. Department-wise Employees
9. Exit
```

---

## Salary Calculation Logic

### Bonus

| Salary | Bonus |
|---------|-------|
| ≥ 50,000 | 10% |
| < 50,000 | 5% |

### Tax

| Salary | Tax |
|---------|-----|
| ≥ 70,000 | 15% |
| 40,000 – 69,999 | 10% |
| < 40,000 | 5% |

### Formula

```
Net Salary = Salary + Bonus - Tax
```

---

## SQL Operations Used

- INSERT
- SELECT
- UPDATE
- DELETE
- WHERE
- ORDER BY
- LIMIT

---

## Python Concepts Used

- Classes & Objects
- Functions
- Conditional Statements
- Loops
- Lists
- Exception Handling
- MySQL Connectivity
- CRUD Operations
- Parameterized SQL Queries

---

## Future Enhancements

- Employee Login System
- Attendance Management
- Leave Management
- Salary Slip Generation
- Export Reports to Excel/PDF
- GUI using Tkinter or Streamlit
- Role-Based Authentication

---

## Requirements

Install the required package:

```bash
pip install mysql-connector-python
```

or

```bash
pip install -r requirements.txt
```

---

## Author

**Preetham**

Artificial Intelligence & Machine Learning Student

GitHub: https://github.com/Preetham-18

---

## License

This project is developed for educational and learning purposes.

---

⭐ If you found this project useful, consider giving it a star on GitHub.
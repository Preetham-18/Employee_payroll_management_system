# Create the database
CREATE DATABASE employee_payroll;

# Use the database
USE employee_payroll;

# Creating employee table
CREATE TABLE employee (
    employee_id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT NOT NULL,
    dept VARCHAR(50),
    designation VARCHAR(50),
    salary FLOAT
);
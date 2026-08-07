import mysql.connector

def connect_database():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Your_password_here",  # Replace with your MySQL root password
        database="Your_database_name_here"  # Replace with your database name
    )
    return connection

connection = connect_database()
cursor = connection.cursor()


class Employee:
    def __init__(self, employee_id, name, age, dept, designation, salary):
        self.employee_id = employee_id
        self.name = name
        self.age = age
        self.dept = dept
        self.designation = designation
        self.salary = salary


def calculate_salary(emp):
        bonus = 0
        tax = 0
        net_salary = 0

        if emp.salary >= 50000:
            bonus = emp.salary*10/100
        else:
            bonus = emp.salary*5/100

        if emp.salary >= 70000:
            tax = emp.salary*15/100
        elif emp.salary >= 40000:
            tax = emp.salary*10/100
        else:
            tax = emp.salary*5/100

        net_salary = emp.salary + bonus - tax

        return bonus, tax, net_salary


print("=" *40)
print("EMPLOYEE PAYROLL MANAGEMENT SYSTEM")
print("=" *40)

choice = ""
while choice != "9":
    print("1. Add employee ")
    print("2. View employees")
    print("3. Search employee")
    print("4. Update employee")
    print("5. Delete employee")
    print("6. Calculate salary")
    print("7. Highest paid employee")
    print("8. Dept. wise employees")
    print("9. Exit")

    choice = input(" Enter your choice: ")

    if choice == "1":
        employee_id = int(input("Enter employee_id:"))
        name = input("Enter employee name: ")
        age = int(input("Enter employee age:"))
        dept = input("Enter employee dept:")
        designation = input("Enter employee designation:")
        salary = int(input("Enter employee salary:"))

        query = """
        INSERT INTO employee (employee_id, name, age, dept, designation, salary)
        VALUES (%s, %s, %s, %s, %s, %s)
        """

        try:
            cursor.execute(query, (employee_id, name, age, dept, designation, salary))
            connection.commit()
            print("Employee Added successfully")
        except mysql.connector.Error as err:
            print(err)
        print()
    elif choice == "2":
       print("------VIEW EMPLOYEES------")

       query = """SELECT * FROM employee"""

       cursor.execute(query)
       employees = cursor.fetchall()

       if not employees:
              print("No employees found")
       else:
            for emp in employees:
                print("----------------------")
                print("Employee id: ", emp[0])
                print("Name: ", emp[1])
                print("Age: ", emp[2])
                print("Dept: ", emp[3])
                print("Designation: ", emp[4])
                print("Salary: ", emp[5])

       print()
    
        
    elif choice == "3": 
        employee_id = int(input("Enter employee_id:"))   

        query = """SELECT * FROM employee WHERE employee_id = %s """

        cursor.execute(query,(employee_id,))
        emp = cursor.fetchone()

        if not emp:
            print("Employee not found")
        else:
            print("----------------------")
            print("Employee id: ", emp[0])
            print("Name: ", emp[1])
            print("Age: ", emp[2])
            print("Dept: ", emp[3])
            print("Designation: ", emp[4])
            print("Salary: ", emp[5])

        print()
    elif choice == "4":
        employee_id = int(input("Enter employee_id:"))


        query = """SELECT * FROM employee WHERE employee_id = %s """

        cursor.execute(query,(employee_id,))
        emp = cursor.fetchone()

        if not emp:
            print("Employee not found")
        else:
            print("1. Update name")
            print("2. Update age")
            print("3. Update Dept")
            print("4. Update salary")
            print("5. Update designation")

            update_choice = input("Enter your choice:")

            if update_choice == "1":
                new_name = input("Enter new name:")
                query = """UPDATE employee SET name = %s WHERE employee_id = %s"""

                cursor.execute(query,( new_name, employee_id))
                connection.commit()
                print("Name updated successfully")
            elif update_choice == "2":
                new_age = int(input("Enter new age:"))
                query = """UPDATE employee SET age = %s WHERE employee_id = %s"""

                cursor.execute(query,(new_age, employee_id))
                connection.commit()
                print("Age updated successfully")
            elif update_choice ==  "3":
                new_dept = input("Enter new dept:")
                query = """UPDATE employee SET dept = %s WHERE employee_id = %s"""

                cursor.execute(query,(new_dept, employee_id))
                connection.commit()

                print("Dept updated successfully")
            elif update_choice == "4":
                new_salary = int(input("Enter new salary:"))
                query = """UPDATE employee SET salary = %s WHERE employee_id = %s"""

                cursor.execute(query,(new_salary, employee_id))
                connection.commit()
                print("Salary updated successfully")
            elif update_choice == "5":
                new_designation = input("Enter new designation:")
                query = """UPDATE employee SET designation = %s WHERE employee_id = %s"""

                cursor.execute(query,(new_designation, employee_id))
                connection.commit()
                print("Designation updated successfully")
            else:
                print("Invalid choice")
            
        print()
    elif choice == "5":
        employee_id = int(input("Enter employee_id:"))

        query = """DELETE FROM employee WHERE employee_id = %s"""

        cursor.execute(query,(employee_id,))

        connection.commit()

        if cursor.rowcount == 0:
            print("Employee not found")
        else:
            print("Employee deleted successfully")
        print()
    elif choice == "6":
        employee_id = int(input("Enter employee_id:"))

        query = """SELECT * FROM employee WHERE employee_id = %s"""

        cursor.execute(query,(employee_id,))

        emp = cursor.fetchone()

        if not emp:
            print("Employee not found")
        else:
            employee = Employee(emp[0], emp[1], emp[2], emp[3], emp[4], emp[5])
            bonus, tax, net_salary = calculate_salary(employee)

            print("Name: ", employee.name)
            print("Salary: ", employee.salary)
            print("Bonus: ", bonus)
            print("Tax: ", tax)
            print("Net Salary: ", net_salary)
        print()
    elif choice == "7":

        query = """SELECT * FROM employee ORDER BY salary DESC LIMIT 1"""

        cursor.execute(query)
        employee = cursor.fetchone()

        if not employee:
            print("Employee not found")
        else:
            print("Employee_id:", employee[0])
            print("Name :", employee[1])
            print("Age:", employee[2])
            print("Dept:", employee[3])
            print("Designation:", employee[4])
            print("Salary:", employee[5])

        print()
    elif choice == "8":
        print("Dept.wise employees")
        dept = input("Enter dept name:")

        query = """SELECT * FROM employee WHERE dept = %s"""
        cursor.execute(query,(dept,))
        employees = cursor.fetchall()

        if not employees:
            print("Employee not found")
        else:
            for emp in employees:
                print("Employee id: ", emp[0])
                print("Name: ", emp[1])
                print("Age: ", emp[2])
                print("Dept: ", emp[3])
                print("Designation: ", emp[4])
                print("Salary: ", emp[5])

        print()
    elif choice == "9":

        cursor.close()
        connection.close()
        print("Thank you for using Employee Payroll Management System")
        print()
    else:
        print("Invalid choice")
     
    
    
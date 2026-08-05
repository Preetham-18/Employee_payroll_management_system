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

employees = []


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
        designation = input("enter employee designation:")
        salary = int(input("Enter employee salary:"))
        emp = Employee(employee_id, name, age, dept, designation, salary)
        employees.append(emp)
        print("Employee Added successfully")
        print()
    elif choice == "2":
        print("----View employees----")
        print("----------------------")
        if not employees:
            print("No employees found")
        for emp in employees:
            print("----------------------")
            print("Employee id: ", emp.employee_id)
            print("Name: ", emp.name)
            print("Age: ", emp.age)
            print("Dept: ", emp.dept)
            print("Designation: ", emp.designation)
            print("Salary: ", emp.salary)
        print("----------------------")
    elif choice == "3":    
        employee_id = int(input("Enter employee_id:"))
        found = False
        for emp in employees:
            if employee_id == emp.employee_id:
                found = True
                print("Employee id: ", emp.employee_id)
                print("Name: ", emp.name)
                print("Age: ", emp.age)
                print("Dept: ", emp.dept)
                print("Designation: ", emp.designation)
                print("Salary: ", emp.salary)
                
                break
        if not found:
            print("Employees Not Found ")
        print()
    elif choice == "4":
        employee_id = int(input("Enter employee_id:"))
        found = False
        for emp in employees:
            if employee_id == emp.employee_id:
                found = True
                print("1. Update name")
                print("2. Update age")
                print("3. Update Dept")
                print("4. Update salary")

                update_choice = input("Enter your choice:")

                if update_choice == "1":
                    emp.name = input("Enter new name:")
                    print("Name updated")
                elif update_choice == "2":
                    emp.age = int(input("Enter new age:"))
                    print("Age updated")
                elif update_choice == "3":
                    emp.dept = input("Enter new dept:")
                    print("Dept updated")
                elif update_choice == "4":
                    emp.salary = int(input("Enter new salary:"))
                    print("Salary updated")
                else:
                    print("Invalid choice")
                    
                break
        if not found:
            print("Employee not found")
        print()
    elif choice == "5":
        employee_id = int(input("Enter employee_id:"))
        found = False
        for emp in employees:
            if employee_id == emp.employee_id:
                found = True
                employees.remove(emp)
                print("Deleted successfully")
                
                break

        if not found:
            print("Employee not found")
        print()
    elif choice == "6":
        employee_id = int(input("Enter employee_id:"))
        found = False
        for emp in employees:
            if employee_id == emp.employee_id:
                found = True
                bonus, tax, net_salary = calculate_salary(emp)
                print("Name :", emp.name)
                print("Salary: ", emp.salary)
                print("Bonus: ", bonus)
                print("Tax:", tax)
                print("Net_salary:", net_salary)
                break
        if not found:
            print("Employee not found")
        print()
    elif choice == "7":
        print("Highest paid Employee is :")
        if not employees:
            print("No employees found")
        else:
            highest = employees[0]
            for emp in employees:
                if emp.salary > highest.salary:
                    highest = emp

            print("Employee_id:", highest.employee_id)
            print("Name :", highest.name)
            print("AGe:", highest.age)
            print("Dept:", highest.dept)
            print("Designation:", highest.designation)
            print("Salary:", highest.salary)
                
        print()
    elif choice == "8":
        print("Dept.wise employees")
        dept = input("Enter dept name:")
        found = False
        for emp in employees:
            if emp.dept == dept:
                found = True
                print("Employee id: ", emp.employee_id)
                print("Name: ", emp.name)
                print("Age: ", emp.age)
                print("Dept: ", emp.dept)
                print("Designation: ", emp.designation)
                print("Salary: ", emp.salary)
        if not found:
            print("Employee not found")
        print()
    elif choice == "9":
        print("Thank you fro using Employee payroll management system")
        print()
    else:
        print("Invalid choice")
     
    
    
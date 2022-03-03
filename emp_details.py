employers = int(input("Enter the num of employees: "))
employee_name = []
employee_age = []
employee_designation = []
employee_salary = []
for i in range(0, employers):
    name = input("Enter the name of the employee: ")
    age = int(input("Enter the age of the employee: "))
    designation = input("Enter the designation of an employee: ")
    salary = int(input("Enter the expected or current salary of the employee: "))
    employee_name.append(name)
    employee_age.append(age)
    employee_designation.append(designation)
    employee_salary.append(salary)
print(employee_name)
print(employee_age)
print(employee_designation)
print(employee_salary)
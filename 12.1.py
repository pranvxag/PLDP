# Assignment 12: Class with method to calculate yearly salary

class Employee:
    def __init__(self, name, monthly_salary):
        self.name = name
        self.monthly_salary = monthly_salary

    def calculate_yearly_salary(self):
        return self.monthly_salary * 12


# Taking input
name = input("Enter employee name: ")
monthly_salary = float(input("Enter monthly salary: "))

# Creating object
emp = Employee(name, monthly_salary)

# Display result
print("Employee Name:", emp.name)
print("Yearly Salary:", emp.calculate_yearly_salary())
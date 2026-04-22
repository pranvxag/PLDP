# Add a new employee record to the existing list

class Employee:
    def __init__(self, name, department, salary):
        self.name = name
        self.department = department
        self.salary = salary

    def display(self):
        print(f"Name: {self.name}, Department: {self.department}, Salary: {self.salary}")


# Existing employee list
employees = [
    Employee("Pranav", "IT", 30000),
    Employee("Karthik", "HR", 25000)
]

# Taking input for new employee
name = input("Enter employee name: ")
department = input("Enter department: ")
salary = float(input("Enter salary: "))

# Creating new employee object
new_emp = Employee(name, department, salary)

# Adding to list
employees.append(new_emp)

print("\nUpdated Employee List:\n")

# Display all employees
for emp in employees:
    emp.display()
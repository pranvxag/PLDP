# Assignment 12: Filter employees by department

class Employee:
    def __init__(self, name, department, salary):
        self.name = name
        self.department = department
        self.salary = salary

    def display(self):
        print(f"Name: {self.name}, Department: {self.department}, Salary: {self.salary}")


# Create list of employees
employees = [
    Employee("Pranav", "IT", 30000),
    Employee("Karthik", "HR", 25000),
    Employee("Amit", "IT", 40000),
    Employee("Neha", "Finance", 35000)
]

# Take department input
dept = input("Enter department to filter: ")

print("\nEmployees in", dept, "department:\n")

found = False
for emp in employees:
    if emp.department.lower() == dept.lower():
        emp.display()
        found = True

if not found:
    print("No employees found in this department.")
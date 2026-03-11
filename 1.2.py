# Calculator for Subtraction and Division

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Subtraction:", a - b)

if b != 0:
    print("Division:", a / b)
else:
    print("Division not possible (division by zero)")

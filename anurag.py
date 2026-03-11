# Program to find remainder

# Input two numbers
num1 = int(input("Enter the dividend: "))
num2 = int(input("Enter the divisor: "))

# Check division by zero
if num2 != 0:
    remainder = num1 % num2
    print("Remainder:", remainder)
else:
    print("Division by zero is not allowed")
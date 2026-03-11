# Compound Interest Calculator

P = float(input("Enter Principal (P): "))
r = float(input("Enter Rate of Interest (r): "))
n = float(input("Enter number of times interest is compounded per year (n): "))
t = float(input("Enter Time in years (t): "))

A = P * (1 + r/n) ** (n * t)

print("Amount (A):", A)
print("Compound Interest:", A - P)

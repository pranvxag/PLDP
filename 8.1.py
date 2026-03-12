n = int(input("Enter number of elements in tuple: "))
t = []

for i in range(n):
    t.append(float(input("Enter value: ")))

t = tuple(t)

result = sorted(t)[:5]

print("Minimum 5 elements:", result)

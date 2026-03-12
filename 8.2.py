n = int(input("Enter number of elements in tuple: "))
t = []

for i in range(n):
    t.append(float(input("Enter value: ")))

k = int(input("Enter value of k: "))

t = tuple(t)

result = sorted(t)[:k]

print("Minimum elements:", result)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

total = 0
for row in matrix:
    for num in row:
        total = total + num

print("Sum of all elements in matrix:", total)

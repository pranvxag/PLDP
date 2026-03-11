# Input matrix size
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

# Input matrix
print("Enter matrix elements:")
matrix = []

for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input(f"Element [{i}][{j}]: ")))
    matrix.append(row)

# Find transpose
transpose = []

for i in range(cols):
    row = []
    for j in range(rows):
        row.append(matrix[j][i])
    transpose.append(row)

# Initialize result matrix (rows x rows)
result = [[0 for _ in range(rows)] for _ in range(rows)]

# Multiply matrix × transpose
for i in range(rows):
    for j in range(rows):
        for k in range(cols):
            result[i][j] += matrix[i][k] * transpose[k][j]

# Display result
print("\nResultant Matrix (Matrix × Transpose):")
for row in result:
    print(row)
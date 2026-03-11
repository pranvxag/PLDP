# Input first matrix
print("Enter elements of Matrix 1 (3x3):")
A = []

for i in range(3):
    row = []
    for j in range(3):
        row.append(int(input(f"A[{i}][{j}]: ")))
    A.append(row)


# Input second matrix
print("\nEnter elements of Matrix 2 (3x3):")
B = []

for i in range(3):
    row = []
    for j in range(3):
        row.append(int(input(f"B[{i}][{j}]: ")))
    B.append(row)


# Initialize result matrix with zeros
result = [[0 for _ in range(3)] for _ in range(3)]


# Matrix multiplication
for i in range(3):
    for j in range(3):
        for k in range(3):
            result[i][j] += A[i][k] * B[k][j]


# Display result
print("\nResultant Matrix (A × B):")
for row in result:
    print(row)
# Input matrix size
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

# Function to take matrix input
def input_matrix(name):
    print(f"\nEnter elements of {name}:")
    matrix = []

    for i in range(rows):
        row = []
        for j in range(cols):
            val = int(input(f"Enter element [{i}][{j}]: "))
            row.append(val)
        matrix.append(row)

    return matrix


# Function to check if all elements are even
def check_even(matrix):
    for row in matrix:
        for num in row:
            if num % 2 != 0:
                return False
    return True


# Input matrices
matrix1 = input_matrix("Matrix 1")
matrix2 = input_matrix("Matrix 2")

# Check even condition
if check_even(matrix1) and check_even(matrix2):

    # Add matrices
    result = []

    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)

    # Print result
    print("\nResultant Matrix (Addition):")
    for row in result:
        print(row)

else:
    print("\nMatrix addition not possible because one or more elements are odd.")
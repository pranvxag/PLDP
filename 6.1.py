import numpy as np

user_input = input("Enter numbers separated by spaces: ")
arr = np.array([int(x) for x in user_input.split()])

total = arr.sum()
print(f"\nArray: {arr}")
print(f"Sum: {total}")

# For 2D array input
print("\n--- 2D Array ---")
rows = int(input("Enter number of rows: "))
matrix = []

for i in range(rows):
    row_input = input(f"Enter row {i+1} numbers separated by spaces: ")
    row = [int(x) for x in row_input.split()]
    matrix.append(row)

arr_2d = np.array(matrix)

print(f"\n2D Array:\n{arr_2d}")
print(f"Sum of all elements: {arr_2d.sum()}")
print(f"Sum along rows (axis=0): {arr_2d.sum(axis=0)}")
print(f"Sum along columns (axis=1): {arr_2d.sum(axis=1)}")

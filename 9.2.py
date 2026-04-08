# Bubble Sort (based on marks)

def bubble_sort_students(arr):
    n = len(arr)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            
            # Compare marks (index 1 of tuple)
            if arr[j][1] > arr[j + 1][1]:
                # Swap
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    return arr


# Example
students = [("Pranav", 85), ("Riya", 92), ("Karthik", 78)]
sorted_students = bubble_sort_students(students)

print("Sorted by marks:", sorted_students)

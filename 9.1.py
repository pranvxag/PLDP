# Selection Sort

def selection_sort(arr):
    n = len(arr)
    
    for i in range(n):
        # Assume current position has the minimum
        min_index = i
        
        # Find actual minimum in remaining list
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Swap
        arr[i], arr[min_index] = arr[min_index], arr[i]
    
    return arr


# Example
numbers = [64, 25, 12, 22, 11]
sorted_numbers = selection_sort(numbers)

print("Sorted list:", sorted_numbers)

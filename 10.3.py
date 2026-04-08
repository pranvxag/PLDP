#Binary Search Code

def binary_search(arr, key):
    low = 0
    high = len(arr) - 1
    comparisons = 0
    
    while low <= high:
        mid = (low + high) // 2
        comparisons += 1
        
        if arr[mid] == key:
            return mid, comparisons
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1, comparisons

#Fibonacci Search Code
def fibonacci_search(arr, key):
    n = len(arr)
    
    fib2 = 0
    fib1 = 1
    fib = fib1 + fib2
    
    while fib < n:
        fib2 = fib1
        fib1 = fib
        fib = fib1 + fib2
    
    offset = -1
    comparisons = 0
    
    while fib > 1:
        i = min(offset + fib2, n - 1)
        comparisons += 1
        
        if arr[i] < key:
            fib = fib1
            fib1 = fib2
            fib2 = fib - fib1
            offset = i
        
        elif arr[i] > key:
            fib = fib2
            fib1 = fib1 - fib2
            fib2 = fib - fib1
        
        else:
            return i, comparisons
    
    if fib1 and arr[offset + 1] == key:
        return offset + 1, comparisons
    
    return -1, comparisons

#Example Comparison
arr = [10, 20, 30, 40, 50, 60, 70]
key = 50

b_index, b_comp = binary_search(arr, key)
f_index, f_comp = fibonacci_search(arr, key)

print("Binary Search -> Index:", b_index, "Comparisons:", b_comp)
print("Fibonacci Search -> Index:", f_index, "Comparisons:", f_comp)

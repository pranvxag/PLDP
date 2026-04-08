# Linear Search - First Occurrence

def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i   # return index of first occurrence
    return -1


# Example
numbers = [10, 20, 30, 20, 40]
key = 20

result = linear_search(numbers, key)

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")

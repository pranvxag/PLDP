# Function to convert date string into comparable tuple
def parse_date(date):
    day, month, year = map(int, date.split('-'))
    return (year, month, day)


# Merge function
def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if parse_date(left[i]) < parse_date(right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result


# Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)


# Example
dates = ["12-05-2023", "01-01-2022", "25-12-2021"]
sorted_dates = merge_sort(dates)

print("Sorted dates:", sorted_dates)

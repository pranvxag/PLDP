# Ternary Search for Maximum (Unimodal Array)

def ternary_search_max(arr, left, right):
    while right - left > 2:
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3
        
        if arr[mid1] < arr[mid2]:
            left = mid1
        else:
            right = mid2
    
    # Find max in remaining small range
    return max(arr[left:right+1])


# Example (temperature data)
temps = [10, 15, 20, 25, 30, 28, 24, 18]

max_temp = ternary_search_max(temps, 0, len(temps)-1)

print("Maximum temperature:", max_temp)

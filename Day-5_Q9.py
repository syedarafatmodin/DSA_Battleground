def find_peak(arr):
    start, end = 0, len(arr) - 1
    
    while start < end:
        mid = (start + end) // 2
        
        if arr[mid] > arr[mid + 1]:  
            end = mid  # Peak is in the left half
        else:
            start = mid + 1  # Peak is in the right half
    
    return start  # Both start and end point to the peak



#test case
print(find_peak([1, 2, 3, 1]))  
print(find_peak([1, 2, 1, 3, 5, 6, 4])) 

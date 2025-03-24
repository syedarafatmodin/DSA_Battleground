import bisect

def kClose(nums, k, target):
    pos = bisect.bisect_left(nums, target)  # Find the position to insert target
    left, right = pos - 1, pos  

    while k > 0:
        if left < 0:  
            right += 1  
        elif right >= len(nums) or abs(nums[left] - target) <= abs(nums[right] - target):
            left -= 1  
        else:
            right += 1  
        k -= 1  

    return nums[left + 1:right]  # Return k closest numbers

#test cases
print(kClose([1,2,3,4,5], 4, 3))  
print(kClose([1,1,2,3,4,5], 4, -1))  



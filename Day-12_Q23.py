def minSubArrayLen(target, nums):
    left = 0
    total = 0
    min_length = float('inf')

    for right in range(len(nums)):
        total += nums[right]
        
        while total >= target:
            min_length = min(min_length, right - left + 1)
            total -= nums[left]
            left += 1

    return min_length if min_length != float('inf') else 0

# Test Cases
print(minSubArrayLen(7, [2,3,1,2,4,3]))  
print(minSubArrayLen(4, [1,4,4]))        
print(minSubArrayLen(11, [1,1,1,1,1,1])) 

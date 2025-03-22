def maximumGap(nums):
    if len(nums) < 2:
        return 0
    nums.sort()
    max_gap = 0
    for i in range(1, len(nums)):
        max_gap = max(max_gap, nums[i] - nums[i - 1])
    return max_gap

# Test cases
print(maximumGap([3, 6, 9, 1]))  
print(maximumGap([10]))          

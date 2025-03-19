def min_difference(nums, k):
    if k == 1:
        return 0
    
    nums.sort()
    min_diff = float('inf')

    for i in range(len(nums) - k + 1):
        min_diff = min(min_diff, nums[i + k - 1] - nums[i])

    return min_diff


print(min_difference([90], 1))  
print(min_difference([9,4,1,7], 2)) 

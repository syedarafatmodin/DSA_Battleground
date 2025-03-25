def checkSubarraySum(nums, k):
    remainder_map = {0: -1}  
    prefix_sum = 0
    for i, num in enumerate(nums):
        prefix_sum += num
        remainder = prefix_sum % k
        if remainder in remainder_map:
            if i - remainder_map[remainder] >= 2:
                return True
        else:
            remainder_map[remainder] = i
    return False

#test cases
print(checkSubarraySum([23,2,4,6,7], 6))  
print(checkSubarraySum([23,2,6,4,7], 6))  
print(checkSubarraySum([23,2,6,4,7], 13)) 
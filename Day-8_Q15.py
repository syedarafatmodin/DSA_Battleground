def canJump(nums):
    max_reach = 0  # Track the farthest we can go
    for i, jump in enumerate(nums):
        if i > max_reach:
            return False  # If we can't reach index i, return False
        max_reach = max(max_reach, i + jump)  # Update max reach
    return True  # If we reach the last index, return True

#test cases
print(canJump([2,3,1,1,4]))  
print(canJump([3,2,1,0,4]))  
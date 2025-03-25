def remove_extra(nums):
    if not nums:
        return 0  # Return 0 for an empty list

    index = 0  # Pointer to track position of next valid element
    for num in nums:
        if index < 2 or num != nums[index - 2]:  # Allow each number at most twice
            nums[index] = num
            index += 1
    return index  # Return the new length of the list

#test Cases
nums1 = [1,1,1,2,2,3]
size1 = remove_extra(nums1)
print(size1, nums1[:size1])  

nums2 = [0,0,1,1,1,1,2,3,3]
size2 = remove_extra(nums2)
print(size2, nums2[:size2])  


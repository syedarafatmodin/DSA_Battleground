def search_range(nums: list[int], target: int) -> list[int]:
    def binary_search(left_search):
        left, right = 0, len(nums) - 1
        result = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                result = mid
                if left_search:
                    right = mid - 1  # Move left to find first occurrence
                else:
                    left = mid + 1   # Move right to find last occurrence
        return result

    return [binary_search(True), binary_search(False)]


print(search_range([5,7,7,8,8,10], 8))  
print(search_range([5,7,7,8,8,10], 6))  
print(search_range([], 0))              
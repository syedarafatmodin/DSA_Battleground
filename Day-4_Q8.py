def min_subarray(target, arr):
    start = 0
    total = 0
    min_len = float('inf')

    for end in range(len(arr)):
        total += arr[end]

        while total >= target:
            min_len = min(min_len, end - start + 1)
            total -= arr[start]
            start += 1

    return min_len if min_len != float('inf') else 0

test_cases = [
    (7, [2, 3, 1, 2, 4, 3]),  
    (4, [1, 4, 4]),           
    (11, [1, 1, 1, 1, 1, 1]), 
]
for target, arr in test_cases:
    print(f"Target: {target}, Array: {arr} → Min Subarray Length: {min_subarray(target, arr)}")

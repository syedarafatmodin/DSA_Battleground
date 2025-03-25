def sequentialDigits(low, high):
    sample = "123456789"
    result = []
    for length in range(2, 10):
        for start in range(10 - length):
            num = int(sample[start: start + length])
            if low <= num <= high:
                result.append(num)
    return result

# Test Cases
print(sequentialDigits(100, 300))      
print(sequentialDigits(1000, 13000))  
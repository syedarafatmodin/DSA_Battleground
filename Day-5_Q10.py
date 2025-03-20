#Largest number

from functools import cmp_to_key

def form_largest_number(numbers):
    numbers = list(map(str, numbers))
    
    def compare(a, b):
        return 1 if a + b < b + a else -1  
    
    numbers.sort(key=cmp_to_key(compare))
    
    result = "".join(numbers)
    
    return result if result[0] != "0" else "0"

print(form_largest_number([10, 2]))       
print(form_largest_number([3, 30, 34, 5, 9]))  

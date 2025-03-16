def filter_strings(lst, k, m):
    vowels = {'a', 'e', 'i', 'o', 'u'} 
    result = []

    for word in lst:
        vowel_count = sum(1 for letter in word if letter in vowels)

        if len(word) >= k and vowel_count >= m: 
            result.append(word)

    return result

print(filter_strings(["apple", "hi", "world", "yes", "python"], 4, 2))
print(filter_strings(["education", "science", "art", "mathematics"], 5, 3))
def longest_substring(s):
    char = set()
    left = max_length = 0
    
    for right in range(len(s)):
        while s[right] in char:
            char.remove(s[left])
            left += 1
        char.add(s[right])
        max_length = max(max_length, right - left + 1)
    return max_length

print(longest_substring(("abcabcbb")))
print(longest_substring("bbbbb")) 
print(longest_substring("pwwkew"))
def longest_substring_two_chars(s: str) -> int:
    start, char_count, max_len = 0, {}, 0

    for end, char in enumerate(s):
        char_count[char] = char_count.get(char, 0) + 1  

        while len(char_count) > 2:
            char_count[s[start]] -= 1
            if not char_count[s[start]]:
                del char_count[s[start]]
            start += 1  

        max_len = max(max_len, end - start + 1)

    return max_len


# Test cases
print(longest_substring_two_chars("eceba"))   
print(longest_substring_two_chars("ccaabbb"))  

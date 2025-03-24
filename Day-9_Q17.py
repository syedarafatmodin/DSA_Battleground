from collections import Counter

def is_subsequence(s, t):
    it = iter(t)
    return all(char in it for char in s)

def findLUSlength(strs):
    freq = Counter(strs)  # Count occurrences of each string
    strs.sort(key=len, reverse=True)  # Sort strings by length (longest first)
    
    for i, s in enumerate(strs):
        if freq[s] == 1:  # Only consider unique strings
            if all(not is_subsequence(s, strs[j]) for j in range(len(strs)) if i != j):
                return len(s)  # Return length of the first valid unique subsequence
    
    return -1  # If no uncommon subsequence is found



#test cases
print(findLUSlength(["aba", "cdc", "eae"]))  
print(findLUSlength(["aaa", "aaa", "aa"])) 



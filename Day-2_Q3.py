def length_of_last_word(s: str) -> int:
    words= s.strip().split() #removing spaces and splitting 
    return len(words[-1]) if words else 0  #getting the last word and counting the word


print(length_of_last_word("Learn Python")) 
print(length_of_last_word("  coding is fun  "))
print(length_of_last_word("   fly me   to   the moon  "))
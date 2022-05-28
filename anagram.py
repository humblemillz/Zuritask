# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here

    if (sorted(first_word) == sorted(second_word)):
        print("true: The words are anagrams.")
    else:
        print("false: The words aren't anagrams.")

    return True


first_word = "below"
second_word = "elbow"
find_anagram(first_word, second_word)

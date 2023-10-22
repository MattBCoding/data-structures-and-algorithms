"""
Exercise:
Write a function that accepts a string that contains all the letters of the
alphabet except one and returns the missing letter. For example, the string
"the quick brown box jumps over a lazy dog" contains all the letters of the
alphabet except the letter "f". Your function should have a complexity of
O(N).
"""


# Solution:
def missing_letter(input_string):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    hash_table = {}
    # iterate through every character in the string
    for i in range(len(input_string)):
        # add each character to the hash table
        hash_table[input_string[i]] = True

    # iterate through every character in the alphabet
    for j in range(len(alphabet)):
        # if the current character is not in the hash table
        if alphabet[j] not in hash_table:
            # return the current character
            return alphabet[j]

    # if we get through the loop without returning a missing letter
    return None


# test the function
my_string = "the quick brown box jumps over a lazy dog"
result = missing_letter(my_string)
print(result)
assert result == "f"

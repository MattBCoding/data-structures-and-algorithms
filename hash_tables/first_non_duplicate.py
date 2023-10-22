"""
Exercise:
Write a function that returns the first non-duplicated character in a string.
For example, the string "minimum" has two characters that only appear once:
the "n" and the "u". The function should return "n" since it appears first.
The function should have an efficiency of O(N).
"""


# Solution:
def first_non_duplicate_char(input_string):
    # create a hash table
    hash_table = {}
    # iterate through every character in the string
    for i in range(len(input_string)):
        # if the current character is in the hash table
        if input_string[i] in hash_table:
            # increment the value of the current character
            hash_table[input_string[i]] += 1
        # if the current character is not in the hash table
        else:
            # add the current character to the hash table
            hash_table[input_string[i]] = 1

    # iterate through every character in the string
    for j in range(len(input_string)):
        # if the current character has a value of 1
        if hash_table[input_string[j]] == 1:
            # return the current character
            return input_string[j]

    # if we get through the loop without returning a non-duplicate
    return None


# test the function
my_string = "minimum"
result = first_non_duplicate_char(my_string)
print(result)
assert result == "n"
second_string = "abracadabra"
result2 = first_non_duplicate_char(second_string)
print(result2)
assert result2 == "c"

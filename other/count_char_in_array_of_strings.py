# Exercise:
"""
Use recursion to write a function that accepts an array of strings and
returns the total number of characters across all the strings. For example,
if the input array is ['ab', 'c', 'def', 'ghij'], the output should be 10
since there are 10 characters in total.
"""


# Solution:
def count_the_chars(arr):
    # base case
    if len(arr) == 0:
        return 0

    # recursive case
    return len(arr[0]) + count_the_chars(arr[1:])


# test the function
my_arr = ["ab", "c", "def", "ghij"]
result = count_the_chars(my_arr)
print(result)  # 10

my_second_arr = ["abc", "def", "ghi", "jkl"]
result = count_the_chars(my_second_arr)
print(result)  # 12

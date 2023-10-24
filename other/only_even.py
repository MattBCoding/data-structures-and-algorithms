"""
Exercise:
Use recursion to write a function that accepts an array of numbers and
returns a new array containing just the even numbers.
"""


# Solution:
def extract_even(arr):
    # base case
    if len(arr) == 0:
        return []

    # recursive case
    if arr[0] % 2 == 0:
        return [arr[0]] + extract_even(arr[1:])
    else:
        return extract_even(arr[1:])


# test the function
my_arr = [1, 2, 3, 4, 5, 6]
result = extract_even(my_arr)
print(result)  # [2, 4, 6]

my_second_arr = [1, 3, 5, 7, 9, 10]
result = extract_even(my_second_arr)
print(result)  # [10]

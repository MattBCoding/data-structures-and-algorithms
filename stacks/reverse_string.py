"""
Exercise:
Write a function that uses a stack to reverse a string. For example, if the
string is "abcde" it should return "edcba".
"""

# Solution:
from stack import Stack


def reverse_string(input_string):
    # create a stack
    stack = Stack()
    # iterate through every character in the string
    for i in range(len(input_string)):
        # push each character onto the stack
        stack.push(input_string[i])

    # create a new string
    new_string = ""
    # while the stack is not empty
    while not stack.is_empty():
        # add each character to the new string
        new_string += stack.pop()

    # return the new string
    return new_string


# test the function
my_string = "abcde"
result = reverse_string(my_string)
print(result)
assert result == "edcba"
second_string = "Hello, world!"
result2 = reverse_string(second_string)
print(result2)
assert result2 == "!dlrow ,olleH"

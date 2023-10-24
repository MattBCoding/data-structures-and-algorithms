# recursive function to reverse a string


def reverse_string(input_string):
    # base case
    if len(input_string) == 1:
        return input_string
    # recursive case
    return reverse_string(input_string[1:]) + input_string[0]


# test the function
my_string = "abcde"
result = reverse_string(my_string)
print(result)
assert result == "edcba"
second_string = "Hello, world!"
result2 = reverse_string(second_string)
print(result2)
assert result2 == "!dlrow ,olleH"

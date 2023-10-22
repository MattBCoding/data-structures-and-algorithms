# A simple function to check if a string is a palindrome


def is_palindrome(string):
    # reverse the string
    reversed_string = string[::-1]
    # if the string is equal to the reversed string
    if string == reversed_string:
        # return True
        return True
    # otherwise
    else:
        # return False
        return False


# test the function
print(is_palindrome("racecar"))
print(is_palindrome("hello"))
print(is_palindrome("madam"))


# A simple function to check if a string is a palindrome
# This function uses a for loop to iterate through the string
# It compares the first and last characters
# And then the second and second-to-last characters
# And so on
def is_palindrome2(string):
    # start the left index at index 0
    left_index = 0
    # start the right index at the last index in the string
    right_index = len(string) - 1

    # Iterate through until left_index reaches the middle of the string
    while left_index < (len(string) / 2):
        # if the character on the left doesn't equal the character
        # on the right, the string is not a palindrome
        if string[left_index] != string[right_index]:
            return False

        # move the left index one to the right
        left_index += 1
        # move the right index one to the left
        right_index -= 1

    # if we get to the middle of the string, the string is a palindrome
    return True


# test the function
print(is_palindrome2("racecar"))
print(is_palindrome2("hello"))
print(is_palindrome2("madam"))

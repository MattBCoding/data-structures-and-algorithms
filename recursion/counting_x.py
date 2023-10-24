# recursive function to count number of x's in a string


def count_x(input_string):
    # base case
    if len(input_string) == 1:
        if input_string[0] == "x":
            return 1
        else:
            return 0

    # recursive case
    if input_string[0] == "x":
        return 1 + count_x(input_string[1:])
    else:
        return count_x(input_string[1:])


# test the function
my_string = "xxhixx"
result = count_x(my_string)
print(result)
assert result == 4

second_string = "xhixhix"
result2 = count_x(second_string)
print(result2)
assert result2 == 3

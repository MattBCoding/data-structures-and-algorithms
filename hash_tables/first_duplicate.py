"""
Exercise:
Write a function that accepts an array of strings and returns the first
duplicate value it finds. For example, if the array is
["a", "b", "c", "d", "c", "e", "f"], the function should return "c", since
it's duplicated within the array. You can assume there is only one duplicate
within the array. Make sure the function has a complexity of O(N).
"""


# Solution:
def first_duplicate(arr):
    # create a hash table
    hash_table = {}
    # iterate through every element in the array
    for i in range(len(arr)):
        # if the current element is in the hash table
        # it means it is a duplicate
        if arr[i] in hash_table:
            # return the current element
            return arr[i]
        # if the current element is not in the hash table
        else:
            # add the current element to the hash table
            hash_table[arr[i]] = True

    # if we get through the loop without returning a duplicate
    # return None
    return None


# test the function
my_list = ["a", "b", "c", "d", "c", "e", "f"]
result = first_duplicate(my_list)
print(result)
assert result == "c"
second_list = ["a", "b", "c", "d", "e", "f"]
result2 = first_duplicate(second_list)
print(result2)
assert result2 == None

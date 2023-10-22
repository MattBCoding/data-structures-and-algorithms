"""
Exercise:
Write a function that returns the intersection of two arrays. The intersection
is a third array that contains all values contained within the first two
arrays. For example, the intersection of [1, 2, 3, 4, 5] and [0, 2, 4, 6, 8]
is [2, 4].
Your function should have a complexity of O(N).
"""


# Solution:
def find_intersection(arr1, arr2):
    # establish holding variables
    larger_array = []
    smaller_array = []
    hash_table = {}
    intersection = []

    # determine which array is smaller and assign to variables
    if len(arr1) > len(arr2):
        larger_array = arr1
        smaller_array = arr2
    else:
        larger_array = arr2
        smaller_array = arr1

    # iterate through every element of the larger array and add to hash table
    for i in range(len(larger_array)):
        hash_table[larger_array[i]] = True

    # iterate through every element of the smaller array
    for i in range(len(smaller_array)):
        # if the current element in the smaller array is in the hash table
        if smaller_array[i] in hash_table:
            # add the current element to the intersection array
            intersection.append(smaller_array[i])

    # return the intersection array
    return intersection


# test the function
arr1 = [1, 2, 3, 4, 5]
arr2 = [0, 2, 4, 6, 8]
correct_intersection = [2, 4]
result = find_intersection(arr1, arr2)
print(result)
# assert keyword - if the condition is true, the program continues
assert result == correct_intersection
# if the condition is false, the program stops and throws an AssertionError

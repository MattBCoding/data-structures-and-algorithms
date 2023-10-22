# How could we write a function that compares two arrays and lets us know if
# one is a subset of the other?

# one way to do it is to use a nested loop.
# we'd iterate through every element of the smaller array, and for each
# element in the smaller array, we'd then begin a second loop that iterates
# through each element of the larger array. If we ever find an element in the
# smaller array that isn't comtained within the larger array, our function
# will return false. If the code gets past the loops, it means it never
# encountered a value in the smaller array that wasn't in the larger array,
# so it returns true.


# O(N * M) time complexity
def is_subset(arr1, arr2):
    larger_array = []
    smaller_array = []

    # determine which array is smaller
    if len(arr1) > len(arr2):
        larger_array = arr1
        smaller_array = arr2
    else:
        larger_array = arr2
        smaller_array = arr1

    # iterate through every element of the smaller array
    for i in range(len(smaller_array)):
        # assume temporarily that the current value from the smaller array
        # is not found in the larger array
        found = False
        # iterate through every element of the larger array
        for j in range(len(larger_array)):
            # if the two values are equal, it means the current value in
            # smaller array is present in the larger array
            if smaller_array[i] == larger_array[j]:
                # set found to True
                found = True
                # break out of the inner loop
                break

        # if the current value in smaller array doesn't exist in larger array
        # return false
        if found == False:
            return False

    # if we get through the loops without returning false, it means every
    # value in the smaller array exists in the larger array, so we return true
    return True


# test the function
arr1 = [1, 2, 3, 4, 5, 6]
arr2 = [6, 5, 4]
arr3 = [7, 8, 9, 10, 11]
result = is_subset(arr1, arr2)
print(result)
result2 = is_subset(arr2, arr3)
print(result2)


# another way to do it is to use a hash table
# in this approach, once identifying the larger array, we iterate through
# every element of the larger array and add each element to a hash table.
# then we iterate through every element of the smaller array and check if
# each element exists in the hash table. If it doesn't, we return false.
# If we get through the loops without returning false, it means every value
# in the smaller array exists in the larger array, so we return true.
# O(N) time complexity
def is_subset_hash_table(arr1, arr2):
    larger_array = []
    smaller_array = []
    hash_table = {}

    # determine which array is smaller
    if len(arr1) > len(arr2):
        larger_array = arr1
        smaller_array = arr2
    else:
        larger_array = arr2
        smaller_array = arr1

    # iterate through every element of the larger array
    for i in range(len(larger_array)):
        # add the current element to the hash table
        hash_table[larger_array[i]] = True

    # iterate through every element of the smaller array
    for i in range(len(smaller_array)):
        # if the current element in the smaller array is not in the hash table
        if smaller_array[i] not in hash_table:
            # return false
            return False

    # if we get through the loops without returning false, it means every
    # value in the smaller array exists in the larger array, so we return true
    return True


# test the function
arr1 = [1, 2, 3, 4, 5, 6]
arr2 = [6, 5, 4]
arr3 = [7, 8, 9, 10, 11]
result3 = is_subset_hash_table(arr1, arr2)
print(result3)
result4 = is_subset_hash_table(arr2, arr3)
print(result4)

# the is_subset_hash_table function is more efficient than the is_subset func
# the is_subset_hash_table function has a time complexity of O(N)
# the is_subset function has a time complexity of O(N * M)
# so using the hash table approach is much more efficient

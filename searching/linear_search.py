import random

# Linear search

# create a list - numbers from 1 to 100
my_list = list(range(1, 101, 1))

# shuffle the list so it is not in order
random.shuffle(my_list)
print(my_list)


# create our linear_search function to search the list for a specific value
# as the list is not in order, we have to search every element in the list
# this is called a linear search
def linear_search(arr, search_value):
    # iterate through every element in the list
    for i in range(len(arr)):
        # if the element is equal to the search value
        if arr[i] == search_value:
            # return the index
            return i
    # if we get here, the search value was not found
    return -1


# call the function
result = linear_search(my_list, 68)
print(result)


# let's change the function to work for an ordered list - in ascending order
def linear_search_ordered_list_asc(arr, search_value):
    # iterate through every element in the list
    for i in range(len(arr)):
        # if the element is equal to the search value
        # return the index of the found element
        if arr[i] == search_value:
            # return the index
            return i
        # if the element is greater than the search value
        # we can stop searching because the list is in ascending order
        # and we know the search value is not in the list
        elif arr[i] > search_value:
            return -1
    # if we get here, the search value was not found
    # and the value was higher than anything in the list
    return -1


# sort the list into ascending order
my_list.sort()
print(my_list)

# call linear_search_ordered_list_asc function
result = linear_search_ordered_list_asc(my_list, 68)
print(result)

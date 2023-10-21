import random

# Selection sort
# Selection sort is a simple sorting algorithm - it is not very efficient
# It works by repeatedly finding the minimum element from the unsorted part of the list
# And putting it at the beginning of the list
# It is called selection sort because it repeatedly selects the next smallest element
# It is not very efficient because it has to iterate through the list many times
# And it has to swap elements many times until the list is sorted
# It is Big O(n^2) - quadratic time complexity
# This means that the number of operations increases quadratically with the number of elements
# If we have 10 elements, we could have to do 100 operations

# create a list - numbers from 1 to 100
my_list = list(range(1, 101, 1))
# shuffle the list so it is not in order
random.shuffle(my_list)
print(my_list)
print("\n\n")


# create our selection_sort function to sort the list
def selection_sort(arr):
    # iterate through every element in the list
    for i in range(len(arr)):
        # define the minimum_index variable
        # this is the index of the smallest element in the unsorted part of the list
        lowest_number_index = i
        # iterate through every element in the unsorted part of the list
        for j in range(i + 1, len(arr)):
            # if the element is less than the element at the minimum_index
            if arr[j] < arr[lowest_number_index]:
                # set the minimum_index to the index of the element
                lowest_number_index = j

        # swap the two elements
        arr[i], arr[lowest_number_index] = arr[lowest_number_index], arr[i]

    # return the sorted list
    return arr


# call the function
result = selection_sort(my_list)
print(result)

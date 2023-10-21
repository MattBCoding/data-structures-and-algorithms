import random

# Bubble sort
# Bubble sort is a simple sorting algorithm - it is not very efficient
# It works by repeatedly swapping the adjacent elements if they are in the wrong order
# It is called bubble sort because the smaller elements gradually bubble to the top of the list
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


# create our bubble_sort function to sort the list
def bubble_sort(arr):
    # define the unsorted_until_index variable - the end of the list
    unsorted_until_index = len(arr) - 1
    # create a boolean variable to track whether the list is sorted
    sorted = False

    # while the list is not sorted
    while not sorted:
        sorted = True
        # iterate through every element in the list once
        for i in range(unsorted_until_index):
            if arr[i] > arr[i + 1]:
                # swap the two elements
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                # set the sorted variable to false as we found something to swap
                sorted = False
        # decrement the unsorted_until_index variable
        # as we have sorted through once, the last element should be in
        # the correct place so we don't need to check it again
        unsorted_until_index -= 1

    # return the sorted list
    return arr


# call the function
result = bubble_sort(my_list)
print(result)

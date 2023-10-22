import random

# Insertion sort
# Insertion sort is a simple sorting algorithm - it is not very efficient
# It works by repeatedly inserting the next element into the correct position
# It is called insertion sort because it inserts the next element into the correct position
# It is not very efficient because it has to iterate through the list many times
# And it has to swap elements many times until the list is sorted
# It is Big O(n^2) - quadratic time complexity
# This means that the number of operations increases quadratically with the number of elements

# create a list - numbers from 1 to 100
my_list = list(range(1, 101, 1))
# shuffle the list so it is not in order
random.shuffle(my_list)
print(my_list)
print("\n\n")


# create our insertion_sort function to sort the list
def insertion_sort(arr):
    # iterate through every element in the list
    # start at index 1 because we compare the current element to the previous element
    # each round of the loop represents a pass-through the list
    for index in range(1, len(arr)):
        # define the temp_value variable
        # this is the element we are removing from the list
        temp_value = arr[index]
        # define the position variable one to the left of the temp_value
        # this is the value we are comparing the temp_value to
        position = index - 1

        # inner loop
        # while the position is greater than or equal to 0
        # can't look in a position less than index 0
        while position >= 0:
            # compare the temp_value to the value at the position
            # if the position value is greater than the temp_value
            if arr[position] > temp_value:
                # shift the position value to the right
                arr[position + 1] = arr[position]
                # move the position one index to the left to compare the
                # previous value to the temp_value
                position = position - 1
            # if the position value is not greater than the temp_value
            else:
                # we break out of the inner loop
                break
        # and insert the temp_value into the correct position
        arr[position + 1] = temp_value

    # return the sorted list
    return arr


sorted = insertion_sort(my_list)
print(sorted)

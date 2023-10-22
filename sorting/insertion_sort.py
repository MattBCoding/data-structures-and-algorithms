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
    for index in range(1, len(arr)):
        # define the current_element variable
        temp_value = arr[index]
        position = index - 1

        while position >= 0:
            if arr[position] > temp_value:
                arr[position + 1] = arr[position]
                position = position - 1
            else:
                break
        arr[position + 1] = temp_value

    # return the sorted list
    return arr


sorted = insertion_sort(my_list)
print(sorted)

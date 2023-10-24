"""
To partition an array is to take a random value from the array - the pivot
and make sure that every number that is less than the pivot ends up to the
left of the pivot and every number that is greater than the pivot ends up
to the right of the pivot.
We accomplish partitioning through a simple algorithm:
"""


def get_pivot(arr, low, high):
    # get the middle index using floor division
    middle = (high + low) // 2
    # set the pivot to the high element as default
    pivot = high
    # if the low element is less than the middle element
    # and the middle element is less than the high element
    if arr[low] < arr[middle] and arr[middle] < arr[high]:
        # set the pivot to the middle element
        pivot = middle
    # else if the low element is less than the high element
    elif arr[low] < arr[high]:
        # set the pivot to the low element
        pivot = low
    # return the pivot
    return pivot


def partition(arr, low, high):
    pivot_index = get_pivot(arr, low, high)
    pivot_value = arr[pivot_index]
    # swap the pivot element with the low element
    arr[pivot_index], arr[low] = arr[low], arr[pivot_index]
    # set the border index
    border = low
    # iterate through the list
    for i in range(low, high + 1):
        # if the element is less than the pivot value
        if arr[i] < pivot_value:
            # increment the border index
            border += 1
            # swap the element with the border element
            arr[i], arr[border] = arr[border], arr[i]
    arr[low], arr[border] = arr[border], arr[low]

    return border

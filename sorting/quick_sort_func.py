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


def quick_sort(arr, low, high):
    # base case
    if low < high:
        # partition the array
        partition_index = partition(arr, low, high)
        # recursively call quick_sort on the left side of the partition
        quick_sort(arr, low, partition_index - 1)
        # recursively call quick_sort on the right side of the partition
        quick_sort(arr, partition_index + 1, high)


def sort_my_array(arr):
    quick_sort(arr, 0, len(arr) - 1)


# test the function
my_arr = [5, 9, 3, 7, 2, 8, 1, 6]
sort_my_array(my_arr)
print(my_arr)  # [1, 2, 3, 5, 6, 7, 8, 9]

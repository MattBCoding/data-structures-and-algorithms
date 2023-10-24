# recursively double each number in an array


def double_array(arr, index=0):
    # Base case: when the index goes past the end of the array
    if index >= len(arr):
        return

    # Recursive case: double the number at the current index
    arr[index] *= 2
    double_array(arr, index + 1)

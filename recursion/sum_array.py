# recursive function to calculate sum of array


def sum_array(arr):
    # base case
    if len(arr) == 1:
        return arr[0]
    # recursive case
    return arr[0] + sum_array(arr[1:])


# test the function
arr = [1, 2, 3, 4, 5]
result = sum_array(arr)
print(result)

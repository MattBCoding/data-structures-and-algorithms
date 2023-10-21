import random

# Binary search
# Binary search is a much more efficient search algorithm than linear search
# It is used on ordered lists only
# It works by dividing the list in half and comparing the search value to the middle element
# It then discards the half of the list that cannot contain the search value


## Binary Search - Generic
def binary_search(lo, hi, condition):
    while lo <= hi:
        mid = (lo + hi) // 2
        result = condition(mid)
        if result == "found":
            return mid
        elif result == "left":
            hi = mid - 1
        else:
            lo = mid + 1
    return -1


# locating a value in an ordered list - ascending order
def locate_value(arr, query):
    # define the condition function
    def condition(mid):
        # if the middle element is equal to the query
        if arr[mid] == query:
            # check if the element to the left is equal to the query
            # this checks for duplicate values
            # if there is a duplicate value, return "left"
            # this will cause the binary search to continue searching the
            # left half of the list for the first occurrence of the value
            if mid > 0 and arr[mid - 1] == query:
                return "left"
            else:
                return "found"
        # if the middle element is greater than the query
        # search the left half of the list for an ascending list
        # change to < for a descending list
        elif arr[mid] > query:
            return "left"
        else:
            return "right"

    return binary_search(0, len(arr) - 1, condition)


# create a list - numbers from 1 to 100
my_list = list(range(1, 101, 1))
# call the function
result = locate_value(my_list, 68)
print(result)

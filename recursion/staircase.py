# recursive function to calculate the total number of paths to climb a
# staircase of n steps, taking steps of size 1, 2, or 3


def count_paths(n):
    # base case
    if n == 1 or n == 0:
        return 1
    elif n < 0:
        return 0
    # recursive case
    return count_paths(n - 1) + count_paths(n - 2) + count_paths(n - 3)


# test the function
n = 3
result = count_paths(n)
print(result)
assert result == 4

n = 4
result = count_paths(n)
print(result)
assert result == 7

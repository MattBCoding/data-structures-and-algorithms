"""
Exercise:
The fibonacci sequence is a mathematical sequence of numbers that goes like
this until infinity: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ... The next number can
be found by adding up the two numbers before it, and the first two numbers are
always 0 and 1. Write a function that accepts a number, n, and returns the nth
number of the fibonacci sequence. For example, if the input was 10, the function
should return 55 since that's the 10th number in the sequence. The first number
0 is considered the 0th number in the sequence. so 1 is the 1st.
"""


# Solution:
def fibonacci(n, memo={}):
    print("fibonacci called")
    # base case
    if n == 0 or n == 1:
        return n

    # check the hash table (called memo) to see if we've already calculated
    # the result for this n
    if not memo.get(n):
        # recursive case
        # if n is NOT in memo, compute fibonacci(n) and store the result in
        # memo[n]
        memo[n] = fibonacci(n - 2, memo) + fibonacci(n - 1, memo)

    # return the result
    # by now, fibonacci(n) is in memo, so we can just return it
    print(memo)
    return memo[n]


# test the function
result = fibonacci(10)
print(result)  # 55

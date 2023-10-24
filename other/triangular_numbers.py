"""
Exercise:
There is a numerical sequence known as 'Triangular Numbers'. The pattern
begins as 1, 3, 6, 10, 15, 21, and continues onward with the Nth number in the
pattern, which is N plus the previous number. For example, the 7th number in
the sequence is 28, since it's 7 (which is N) plus 21 (the previous number).
Write a function that accepts a number N and returns the correct number from
the series. That is, if the function was passed the number 7, it would return
28.
"""


# Solution:
def triangular_number(n):
    # base case
    if n == 1:
        return 1

    # recursive case
    return n + triangular_number(n - 1)


# test the function
result = triangular_number(7)
print(result)  # 28

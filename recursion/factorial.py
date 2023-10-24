# recursive ways to calculate factorial


# top down method
def factorial(n):
    # base case
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


# bottom up method
def alt_factorial(n, i=1, product=1):
    # base case
    if i > n:
        return product
    # recursive case
    return alt_factorial(n, i + 1, product * i)

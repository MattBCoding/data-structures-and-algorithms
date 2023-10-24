def fib(n):
    if n == 0:
        return 0

    # a and b start with the first two numbers in the sequence
    a = 0
    b = 1

    # we use range(n) because we want to loop n times
    for i in range(1, n):
        # a and b each move up to the next numbers in the series.
        # namely, b becomes the sum of b + a, and a becomes the old value of b
        # we utilize a temp variable to make these changes:
        temp = a
        a = b
        b = temp + b

    return b


# test the function
result = fib(10)
print(result)  # 55

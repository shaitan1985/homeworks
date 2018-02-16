def fibonacci(n):
    x = 1
    y = 0
    while n:
        yield x + y
        x, y = y, x + y
        n -= 1

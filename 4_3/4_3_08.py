def fibonacci(count, sep=' '):
    num1 = 0
    num2 = 1
    for _ in range(count):
        yield num1
        num1, num2 = num2, num1 + num2

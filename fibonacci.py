numbers = 20  # amount of numbers to be displayed


def fibonacci(n):  # function for fibonacci sequence
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)  # function formula for fibonacci


if numbers <= 0:
    print("Please enter positive value")  # amount of numbers cannot be less than 1
else:
    for i in range(numbers):  # amount of numbers is 1 or more, so sequence is printed
        print(fibonacci(i))


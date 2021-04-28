repetitions = int(input("Enter number of fibonacci sequence repetitions: "))  # number of reps


def fibonacci(n):  # function for fibonacci sequence
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)  # function formula for fibonacci


if repetitions <= 0:
    print("Please enter positive value")  # number of repetitions cannot be less than 1
else:
    for i in range(repetitions):  # number of reps is 1 or more, so sequence is printed
        print(fibonacci(i))


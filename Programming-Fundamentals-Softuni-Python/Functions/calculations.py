def multiply():
    return num1 * num2


def divide():
    return int(num1 / num2)


def add():
    return num1 + num2


def substract():
    return num1 - num2


operation = input()
num1 = int(input())
num2 = int(input())

if operation == "multiply":
    print(multiply())
elif operation == "divide":
    print(divide())
elif operation == "add":
    print(add())
elif operation == "subtract":
    print(substract())

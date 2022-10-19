def multiplication(one, two, three):
    if (one > 0 and two < 0 and three < 0) or \
        (one < 0 and two > 0 and three < 0) or \
        (one < 0 and two < 0 and three > 0) or \
        (one > 0 and two > 0 and three > 0):
        return "positive"

    elif one < 0 or two < 0 or three < 0:
        return "negative"

    elif one == 0 or two == 0 or three == 0:
        return "zero"

number_one = int(input())
number_two = int(input())
number_three = int(input())

print(multiplication(number_one, number_two, number_three))
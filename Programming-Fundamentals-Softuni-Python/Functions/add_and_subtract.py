def sum_numbers(first, second):
    return first + second


def subtract(sum, third):
    return sum - third


# add_and_subtract()
def main(first, second, third):
    sum_of_first_and_second = sum_numbers(first, second)
    result = subtract(sum_of_first_and_second, third)
    return result


first_num = int(input())
second_num = int(input())
third_num = int(input())

print(main(first_num, second_num, third_num))

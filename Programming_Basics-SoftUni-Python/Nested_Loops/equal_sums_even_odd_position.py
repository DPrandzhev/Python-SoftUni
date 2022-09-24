number_a = int(input())
number_b = int(input())


for current_number in range(number_a, number_b + 1):
    sum_even = 0
    sum_odd = 0
    current_number_as_string = str(current_number)
    for index, digit in enumerate(current_number_as_string):
        if index % 2 == 0:
            sum_odd += int(digit)
        else:
            sum_even += int(digit)
    if sum_odd == sum_even:
        print(current_number, end = " ")

numbers_input = input().split(" ")
abs_number_list = []

for num in numbers_input:
    abs_number_list.append(abs(float(num)))

print(abs_number_list)
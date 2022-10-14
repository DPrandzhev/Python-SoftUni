input_line = input().split(" ")
rounded_list = []


for num in input_line:
    rounded_list.append(round(float(num)))


print(rounded_list)

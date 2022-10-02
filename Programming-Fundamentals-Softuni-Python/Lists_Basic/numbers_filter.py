number_of_lines = int(input())
primary_list = []
filtered_list = []
for i in range(number_of_lines):
    integer = int(input())
    primary_list.append(integer)

command = input()

if command == "even":
    for f in primary_list:
        if f % 2 == 0:
            filtered_list.append(f)
elif command == "odd":
    for f in primary_list:
        if f % 2 != 0:
            filtered_list.append(f)
elif command == "negative":
    for f in primary_list:
        if f < 0:
            filtered_list.append(f)
elif command == "positive":
    for f in primary_list:
        if f >= 0:
            filtered_list.append(f)

print(filtered_list)
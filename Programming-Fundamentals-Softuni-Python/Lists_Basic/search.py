number_n = int(input())
command = input()
my_list = []
filtered_list = []

for lst in range(number_n):
    random_string = input()
    my_list.append(random_string)

    if command in random_string:
        filtered_list.append(random_string)

print(my_list)
print(filtered_list)

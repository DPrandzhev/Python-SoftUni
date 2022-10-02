factor = int(input())
count = int(input())
my_list = []

for num in range(count + 1):
    if num > 0:
        my_list.append(factor * num)

print(my_list)
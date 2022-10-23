input_numbers = [int(x) for x in input().split()]

avg = sum(input_numbers) / len(input_numbers)
max_list = []

input_numbers.sort()
for num in input_numbers[::-1]:
    if num > avg:
        max_list.append(int(num))
        if len(max_list) >= 5:
            break

if len(max_list) <= 0:
    print("No")
else:
    print(*max_list, sep=" ")
import sys

n = int(input())

max_num = -sys.maxsize
sum = 0

for i in range(1, n+1):
    current_num = int(input())

    sum += current_num

    if current_num > max_num:
        max_num = current_num

total_sum = sum - max_num

if total_sum == max_num:
    print("Yes")
    print(f"Sum = {max_num}")

else:
	diff = abs(total_sum - max_num)
	print("No")
	print(f"Diff = {diff}")
amount_numbers = int(input())
odd_sum = 0
even_sum = 0



for place in range(1, amount_numbers + 1):
    current_number = int(input())
    if place % 2 == 0:
        even_sum += current_number
    else:
        odd_sum += current_number

if odd_sum == even_sum:
    print("Yes")
    print(f"Sum = {odd_sum}")

else:
    diff = abs(odd_sum - even_sum)
    print("No")
    print(f"Diff = {diff}")
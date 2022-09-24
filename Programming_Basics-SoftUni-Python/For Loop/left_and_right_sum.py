amount_of_numbers = int(input())
left_side = 0
right_side = 0


for numbers in range(amount_of_numbers * 2):
    current_number = int(input())
    if numbers < amount_of_numbers:
        left_side += current_number
    else:
        right_side += current_number

if left_side == right_side:
    print(f"Yes, sum = {left_side}")
else:
    diff = abs(left_side - right_side)
    print(f"No, diff = {diff}")

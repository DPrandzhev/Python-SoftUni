from sys import maxsize

amount_of_numbers = int(input())
min_number = maxsize
max_number = - maxsize

for numbers in range(amount_of_numbers):
    current_number = int(input())
    if current_number > max_number:
        max_number = current_number
    if current_number < min_number:
        min_number = current_number

print(f"Max number: {max_number}")
print(f"Min number: {min_number}")
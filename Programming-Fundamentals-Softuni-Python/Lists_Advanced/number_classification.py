def positives(num):
    return [number for number in num if int(number) >= 0]
def negatives(num):
    return [number for number in num if int(number) < 0]
def even(num):
    return [number for number in num if int(number) % 2 == 0]
def odd(num):
    return [number for number in num if int(number) % 2 != 0]




some_numbers = input().split(', ')


print(f"Positive: {', '.join(positives(some_numbers))}")
print(f"Negative: {', '.join(negatives(some_numbers))}")
print(f"Even: {', '.join(even(some_numbers))}")
print(f"Odd: {', '.join(odd(some_numbers))}")
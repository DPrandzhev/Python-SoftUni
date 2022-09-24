flowers = input()
amount = int(input())
budget = int(input())
sum = 0

if flowers == "Roses":
    sum = 5 * amount
    if amount > 80:
        sum = sum * 0.9
elif flowers == "Dahlias":
    sum = 3.8 * amount
    if amount > 90:
        sum = sum * 0.85
elif flowers == "Tulips":
    sum = 2.8 * amount
    if amount > 80:
        sum = sum * 0.85
elif flowers == "Narcissus":
    sum = 3 * amount
    if amount < 120:
        sum = sum * 1.15
elif flowers == "Gladiolus":
    sum = 2.5 * amount
    if amount < 80:
        sum = sum * 1.2


diff = abs(budget - sum)

if sum <= budget:
    print(f"Hey, you have a great garden with {amount} {flowers} and {diff:.2f} leva left.")
else:
    print(f"Not enough money, you need {diff:.2f} leva more.")
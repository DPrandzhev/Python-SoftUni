days_to_stay = int(input())
type_room = input()
mark = input()
price = 0
total_sum = 0
nights = days_to_stay - 1

if type_room == "room for one person":
    price = nights * 18
elif type_room == "apartment":
    if days_to_stay < 10:
        price = (nights * 25) * 0.7
    elif days_to_stay < 15:
        price = (nights * 25) * 0.65
    elif days_to_stay > 15:
        price = (nights * 25) * 0.5
elif type_room == "president apartment":
    if days_to_stay < 10:
        price = (nights * 35) * 0.9
    elif days_to_stay < 15:
        price = (nights * 35) * 0.85
    elif days_to_stay > 15:
        price = (nights * 35) * 0.8

if mark == "positive":
    total_sum = price + (price * 0.25)
elif mark == "negative":
    total_sum = price - (price * 0.10)

print(f"{total_sum:.2f}")
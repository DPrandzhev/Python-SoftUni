duration_nights = int(input())
type_of_room = input()
score = input()
price = 0
discount = 0

actual_nights = duration_nights - 1

if type_of_room == "room for one person":
    price = 18 * actual_nights

elif type_of_room == "apartment":
    if actual_nights < 10:
        price = (actual_nights * 25) * 0.7
    elif 10 < actual_nights < 15:
        price = (actual_nights * 25) * 0.65
    elif actual_nights > 15:
        price = (actual_nights * 25) * 0.5

elif type_of_room == "president apartment":
    if actual_nights < 10:
        price = (actual_nights * 35) * 0.1
    elif 10 < actual_nights < 15:
        price = (actual_nights * 35) * 0.85
    elif actual_nights > 15:
        price = (actual_nights * 35) * 0.8


if score == "positive":
    final_price = (price * 0.25) + price
elif score == "negative":
    final_price = price - (price * 0.1)


print(f"{final_price:.2f}")
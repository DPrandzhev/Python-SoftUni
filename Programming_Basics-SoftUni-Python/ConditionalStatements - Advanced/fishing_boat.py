budget = int(input())
season = input()
amount_fisherman = int(input())

price = 0

if season == "Spring":
    price = 3000

if season == "Summer" or season == "Autumn":
    price = 4200

if season == "Winter":
    price = 2600

if amount_fisherman <= 6:
    price = price * 0.9
elif 7 <= amount_fisherman <= 11:
    price = price * 0.85
elif amount_fisherman > 12:
    price = price * 0.75

if amount_fisherman % 2 == 0:
    if season != "Autumn":
        price = price * 0.95

diff = abs(budget - price)
if budget >= price:
    print(f"Yes! You have {diff:.2f} leva left.")
if budget < price:
    print(f"Not enough money! You need {diff:.2f} leva.")
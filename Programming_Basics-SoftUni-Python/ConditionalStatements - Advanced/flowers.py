amount_chrysanthemum = int(input())
amount_roses = int(input())
amount_tulip = int(input())
season = input()
holiday = input()

price_chrysanthemum = 0
price_rose = 0
price_tulip = 0
all_flowers_bouquet = 0

if season == "Spring" or season == "Summer":
    price_chrysanthemum = 2
    price_rose = 4.1
    price_tulip = 2.5
elif season == "Autumn" or season == "Winter":
    price_chrysanthemum = 3.75
    price_rose = 4.5
    price_tulip = 4.15

if holiday == "Y":
    price_chrysanthemum = price_chrysanthemum * 1.15
    price_rose = price_rose * 1.15
    price_tulip = price_tulip * 1.15

all_flowers_bouquet = (price_chrysanthemum * amount_chrysanthemum) + \
                      (price_rose * amount_roses) + \
                      (price_tulip * amount_tulip)

if season == "Spring" and amount_tulip >= 7:
    all_flowers_bouquet = all_flowers_bouquet * 0.95
elif season == "Winter" and amount_roses >= 10:
    all_flowers_bouquet = all_flowers_bouquet * 0.9

if (amount_chrysanthemum + amount_tulip + amount_roses) >= 20:
    all_time_discount = all_flowers_bouquet * 0.2
else:
    all_time_discount = 0

final_price = (all_flowers_bouquet - all_time_discount)

print(f"{(final_price + 2):.2f}")

cake_type = input()
amount_purchased = int(input())
day_of_the_month = int(input())
price = 0
final_price = 0

if day_of_the_month <= 15:
    if cake_type == "Cake":
        price = 24.00
    elif cake_type == "Souffle":
        price = 6.66
    elif cake_type == "Baklava":
        price = 12.60
else:
    if cake_type == "Cake":
        price = 28.70
    elif cake_type == "Souffle":
        price = 9.80
    elif cake_type == "Baklava":
        price = 16.98

price_total = price * amount_purchased

if day_of_the_month > 22:
    final_price = price_total

elif day_of_the_month <= 22:
    if 100 <= price_total <= 200:
        final_price = price_total * 0.85
    else:
        final_price = price_total * 0.75

        if day_of_the_month >= 16:
            final_price = final_price
        else:
            final_price = final_price * 0.9

print(f"{final_price:.2f}")
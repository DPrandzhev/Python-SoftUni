fruit = input()
set_size = input()
amount_purchased = int(input())

price = 0
purchase_total = 0

if set_size == "small":
    if fruit == "Watermelon":
        price = 56 * 2
    elif fruit == "Mango":
        price = 36.66 * 2
    elif fruit == "Pineapple":
        price = 42.10 * 2
    elif fruit == "Raspberry":
        price = 20 * 2

elif set_size == "big":
    if fruit == "Watermelon":
        price = 28.7 * 5
    elif fruit == "Mango":
        price = 19.6 * 5
    elif fruit == "Pineapple":
        price = 24.8 * 5
    elif fruit == "Raspberry":
        price = 15.20 * 5

purchase_total = amount_purchased * price


if purchase_total <= 400:
    price_total = purchase_total
elif purchase_total <= 1000:
    price_total = purchase_total - (purchase_total * 0.15)
else:
    price_total = purchase_total - (purchase_total * 0.5)


print(f"{price_total:.2f} lv.")
from math import ceil
budget = float(input())
command = input()

item_counter = 0
money_spend = 0
while command != "Stop":
    item_purchased = command
    item_price = float(input())
    item_counter += 1
    if item_counter % 3 == 0:
        item_price = item_price / 2

    money_spend += item_price

    if money_spend > budget:
        break

    command = input()

diff = abs(budget - money_spend)
if budget >= money_spend:
    print(f" You bought {item_counter} products for {money_spend:.2f} leva.")
else:
    print(f"You don't have enough money!")
    print(f"You need {diff:.2f} leva!")

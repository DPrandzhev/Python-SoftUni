# import math

budget = float(input())
total_shopping = 0
article_count = 0
command = input()
zero_budget = False


while command != "Stop":
    # current_price = 0
    article_name = command
    article_count += 1
    current_price = float(input())

    if article_count % 3 == 0:
        current_price = 0.5 * current_price
        # total_shopping += current_price

    total_shopping += current_price

        # budget -= total_shopping
    if total_shopping > budget:
        zero_budget = True
        break

        # total_shopping += current_price
        # budget = math.ceil(budget - total_shopping)
    command = input()

if zero_budget:
    diff = abs(budget - total_shopping)
    print("You don't have enough money!")
    print(f"You need {diff:.2f} leva!")
else:
    print(f"You bought {article_count} products for {total_shopping:.2f} leva.")
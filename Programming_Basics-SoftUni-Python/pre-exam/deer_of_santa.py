import math
total_amount_of_absent_days = int(input())
food_left_in_kg = int(input())
food_per_day_d1 = float(input())
food_per_day_d2 = float(input())
food_per_day_d3 = float(input())

food_eaten_d1 = total_amount_of_absent_days * food_per_day_d1
food_eaten_d2 = total_amount_of_absent_days * food_per_day_d2
food_eaten_d3 = total_amount_of_absent_days * food_per_day_d3

total_sum_food = food_eaten_d1 + food_eaten_d2 + food_eaten_d3

diff = abs(food_left_in_kg - total_sum_food)

if total_sum_food > food_left_in_kg:
    print(f"{math.ceil(diff)} more kilos of food are needed.")
else:
    print(f"{math.floor(diff)} kilos of food left.")

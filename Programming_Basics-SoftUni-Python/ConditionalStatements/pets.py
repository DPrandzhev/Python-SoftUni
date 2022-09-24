from math import ceil

number_of_days = int(input())
food_left = int(input())
dog_food = float(input())
cat_food = float(input())
turtle_food = float(input())

# req = required
dog_food_req = number_of_days * dog_food
cat_food_req = number_of_days * cat_food
turtle_food_req = (number_of_days * turtle_food) / 1000

total_food_req = dog_food_req + cat_food_req + turtle_food_req
diff = abs(food_left - total_food_req)

if food_left >= total_food_req:
    print(f"{ceil(diff)} kilos of food left.")
else:
    print(f"{ceil(diff)} more kilos of food are needed.")
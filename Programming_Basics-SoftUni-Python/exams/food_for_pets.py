days_count = int(input())
total_amount_food = float(input())
total_dog_food_eaten = 0
total_cat_food_eaten = 0
dog_total = 0
cat_total = 0
for day in range(1, days_count + 1):
    dog_food = int(input())
    cat_food = int(input())
    total_dog_food_eaten += dog_food
    total_cat_food_eaten += cat_food

    if day % 3 == 0:
        biscuits_amount = (dog_food + cat_food) * 0.10

    grand_total = total_dog_food_eaten + total_cat_food_eaten


p_total = grand_total / total_amount_food * 100
dog_total = total_dog_food_eaten / grand_total * 100
cat_total = total_cat_food_eaten / grand_total * 100

total_percent = 100
if total_amount_food > 0:
    total_percent = grand_total / total_amount_food * 100

print(f"Total eaten biscuits: {round(biscuits_amount)}gr.")

print(f"{total_percent:.2f}% of the food has been eaten.")
print(f"{dog_total:.2f}% eaten from the dog.")
print(f"{cat_total:.2f}% eaten from the cat.")

# days = int(input())
# init_food = float(input())
#
# cat_total = 0
# dog_total = 0
# cookies_total = 0
#
# for day in range(1, days + 1):
#     dog_daily = int(input())
#     cat_daily = int(input())
#     cat_total += cat_daily
#     dog_total += dog_daily
#     if day % 3 == 0:  # cookie day
#         # cookies_total += round((cat_daily + dog_daily) * 0.1)
#         cookies_total += (cat_daily + dog_daily) * 0.1
#
# total = cat_total + dog_total
# cat_percent = cat_total / total * 100
# dog_percent = dog_total / total * 100
#
# total_per = 100
# if init_food > 0:
#     total_per = total / init_food * 100
#
# print(f"Total eaten biscuits: {round(cookies_total)}gr.")
# print(f"{total_per:.2f}% of the food has been eaten.")
# print(f"{dog_percent:.2f}% eaten from the dog.")
# print(f"{cat_percent:.2f}% eaten from the cat.")
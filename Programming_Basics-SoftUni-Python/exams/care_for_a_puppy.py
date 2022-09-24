food_bought = int(input())
command = input()

food_in_grams = food_bought * 1000
total_food_needed = 0

while command != "Adopted":
    food_eaten = int(command)

    total_food_needed += food_eaten

    # if food_in_grams <= 0:
    #     break

    command = input()

diff = abs(total_food_needed - food_in_grams)

if total_food_needed <= food_in_grams:
    print(f"Food is enough! Leftovers: {diff} grams.")
else:
    print(f"Food is not enough. You need {diff} grams more.")
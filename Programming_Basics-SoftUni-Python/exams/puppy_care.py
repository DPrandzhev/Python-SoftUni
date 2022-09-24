food_bought_kg = int(input())
food_in_grams = food_bought_kg * 1000
command = input()
eaten_total = 0

while command != "Adopted":
    grams_eaten = int(command)
    eaten_total += grams_eaten


    command = input()

diff = abs(eaten_total - food_in_grams)
if eaten_total <= food_in_grams:
    print(f"Food is enough! Leftovers: {diff} grams.")
else:
    print(f"Food is not enough. You need {diff} grams more.")
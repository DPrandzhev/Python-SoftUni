days_of_adventure = int(input())
number_of_players = int(input())
group_energy = float(input())
water_per_day_per_person = float(input())
food_per_day_per_person = float(input())
total_water = float(days_of_adventure * number_of_players * water_per_day_per_person)
total_food = float(days_of_adventure * number_of_players * food_per_day_per_person)
water_per_day = 0
food_per_day = 0
for day in range(days_of_adventure):
    energy_used = float(input())
    group_energy -= energy_used
    if group_energy <= 0:
        break
    water_per_day += 1
    if water_per_day >= 2:
        total_water -= total_water * 0.3
        group_energy += group_energy * 0.05
        water_per_day = 0
    food_per_day += 1
    if food_per_day >= 3:
        total_food -= (total_food / number_of_players)
        group_energy += group_energy * 0.1
        food_per_day = 0

if group_energy >= 1:
    print(f"You are ready for the quest. You will be left with - {group_energy:.2f} energy!")
else:
    print(f"You will run out of energy. You will be left with {total_food:.2f} food and {total_water:.2f} water.")
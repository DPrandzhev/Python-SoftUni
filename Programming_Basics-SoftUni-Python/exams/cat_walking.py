minutes_walk_per_day = int(input())
amount_of_walks_day = int(input())
kcal_per_day = int(input())

total_minutes = minutes_walk_per_day * amount_of_walks_day
kcal_burn_per_minute = total_minutes * 5

required_kcal_for_day = kcal_per_day / 2

if kcal_burn_per_minute >= required_kcal_for_day:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {kcal_burn_per_minute}.")

else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {kcal_burn_per_minute}.")
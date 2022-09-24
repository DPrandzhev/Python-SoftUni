percent_fat = int(input())
percent_protein = int(input())
percent_carbohydrates = int(input())
total_amount_kcal = int(input())
percent_water = int(input())

total_grams_fat = ((percent_fat / 100) * total_amount_kcal) / 9
total_grams_protein = ((percent_protein / 100) * total_amount_kcal) / 4
total_grams_carbs = ((percent_carbohydrates / 100) * total_amount_kcal) / 4

total_weight_food = total_grams_fat + total_grams_protein + total_grams_carbs
kcal_per_gram = total_amount_kcal / total_weight_food

sum_water = 100 - percent_water

final_amount = (sum_water / 100) * kcal_per_gram

print(f"{final_amount:.4f}")
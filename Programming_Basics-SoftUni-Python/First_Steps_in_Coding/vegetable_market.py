
price_kg_veg = float(input())
price_kg_fruit = float(input())
total_kg_veg = int(input())
total_kg_fruit = int(input())

sum_lv_veg = (price_kg_veg * total_kg_veg) / 1.94
sum_lv_fruit = (price_kg_fruit * total_kg_fruit) / 1.94

print(f'{sum_lv_fruit+sum_lv_veg:.2f}')

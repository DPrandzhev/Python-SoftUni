budget = float(input())
price_flour = float(input())
price_eggs = price_flour * 0.75
price_milk_l = price_flour * 1.25
price_milk_quarter = price_milk_l / 4
total_price_ingridients = price_flour + price_eggs + price_milk_quarter

loaf_made = 0
colored_eggs = 0
while budget > total_price_ingridients:
    budget -= price_flour
    budget -= price_eggs
    budget -= price_milk_quarter
    loaf_made += 1
    colored_eggs += 3
    if loaf_made % 3 == 0:
        colored_eggs -= (loaf_made - 2)

print(f"You made {loaf_made} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
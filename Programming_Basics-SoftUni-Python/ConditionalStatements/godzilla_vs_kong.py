movie_budget = float(input())
people = int(input())
price_clothes = float(input())
discount_clothes = 0

price_decor = movie_budget * 0.1
price_clothes_all = price_clothes * people

if people >= 150:
    price_clothes_all = price_clothes_all * 0.9

total_budget = price_clothes_all + price_decor
diff = abs(total_budget - movie_budget)

if total_budget > movie_budget:
    print("Not enough money!")
    print(f"Wingard needs {diff:.2f} leva more.")

elif total_budget <= movie_budget:
    print("Action!")
    print(f"Wingard starts filming with {diff:.2f} leva left.")

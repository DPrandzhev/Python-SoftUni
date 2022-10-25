number_of_cities = int(input())
city_name = ''
special_event = True
total_profit = 0
current_profit = 0
for city in range(number_of_cities + 1):
    city_name = input()
    profit = float(input())
    spending_per_city = float(input())
    current_profit = profit - spending_per_city
    if city % 5 == 0:
        special_event = False
        profit *= 0.9
    if city % 2 == 0:
        if special_event:
            spending_per_city *= 1.5
    total_profit += current_profit
    print(f"In {city_name} Burger Bus earned {current_profit:.2f} leva.")

print(f"Burger Bus total profit: {total_profit:.2f} leva.")
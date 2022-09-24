chicken_menu = int(input())
fish_menu = int(input())
vegetarian_menu = int(input())

price_chicken = 10.35
price_fish = 12.40
price_veg = 8.15
price_delivery = 2.50

price_menu = chicken_menu * price_chicken + fish_menu * price_fish + vegetarian_menu * price_veg
price_dessert = price_menu * 0.2

price_total = (price_menu + price_dessert + price_delivery)

print(price_total)

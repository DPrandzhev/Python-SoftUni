lost_fights = int(input())

helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

helm_break = lost_fights // 2
sword_break = lost_fights // 3
shield_break = lost_fights // 6
armor_break = shield_break // 2

expenses = helm_break * helmet_price + sword_break * sword_price + \
           shield_break * shield_price + armor_break * armor_price

print(f"Gladiator expenses: {expenses:.2f} aureus")

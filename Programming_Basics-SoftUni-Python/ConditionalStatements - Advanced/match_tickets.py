# VIP – 499.99 лева.
# Normal – 249.99 лева.

budget = float(input())
category = input()
num_people = int(input())
price_tickets = 0
budget_left = 0

total_sum = 0

if category == "Normal":
    price_tickets = 249.99
elif category == "VIP":
    price_tickets = 499.99

#calculate  budget left based on people:
if num_people <= 4:
    budget_left = budget * 0.25
elif num_people <= 9:
    budget_left = budget * 0.4
elif num_people <= 24:
    budget_left = budget * 0.5
elif num_people <= 49:
    budget_left = budget * 0.60
else:
    budget_left = budget * 0.75

total_sum_tickets = price_tickets * num_people

diff = abs(total_sum_tickets - budget_left)

if total_sum_tickets > budget_left:
    print(f"Not enough money! You need {diff:.2f} leva.")

elif total_sum_tickets <= budget_left:
    print(f"Yes! You have {diff:.2f} leva left.")

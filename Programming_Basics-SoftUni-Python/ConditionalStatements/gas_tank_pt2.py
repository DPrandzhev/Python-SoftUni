fuel_type = input()
fuel_amount = float(input())
discount_card = input()
price = 0

# fuel Gas, Card Yes
if fuel_type == "Gas" and discount_card == "Yes":
    if fuel_amount > 25:
        price = (fuel_amount * 0.85) * 0.9
    elif 20 < fuel_amount <= 25:
        price = (fuel_amount * 0.85) * 0.92
    else:
        price = fuel_amount * 0.85

# fuel Gas, Card No
elif fuel_type == "Gas" and discount_card == "No":
    if fuel_amount > 25:
        price = (fuel_amount * 0.93) * 0.9
    elif 20 < fuel_amount <= 25:
        price = (fuel_amount * 0.93) * 0.92
    else:
        price = fuel_amount * 0.93

#fuel Gasoline, Card Yes
elif fuel_type == "Gasoline" and discount_card == "Yes":
    if fuel_amount > 25:
        price = (fuel_amount * 2.04) * 0.9
    elif 20 < fuel_amount <= 25:
        price = (fuel_amount * 2.04) * 0.92
    else:
        price = fuel_amount * 2.04

#fuel Gasoline, Card No
elif fuel_type == "Gasoline" and discount_card == "No":
    if fuel_amount > 25:
        price = (fuel_amount * 2.22) * 0.9
    elif 20 < fuel_amount <= 25:
        price = (fuel_amount * 2.22) * 0.92
    else:
        price = fuel_amount * 2.22

#Fuel Diesel, Card Yes
elif fuel_type == "Diesel" and discount_card == "Yes":
    if fuel_amount > 25:
        price = (fuel_amount * 2.21) * 0.9
    elif 20 < fuel_amount <= 25:
        price = (fuel_amount * 2.21) * 0.92
    else:
        price = fuel_amount * 2.21

#Fuel Diesel, Card No
elif fuel_type == "Diesel" and discount_card == "No":
    if fuel_amount > 25:
        price = (fuel_amount * 2.33) * 0.9
    elif 20 < fuel_amount <= 25:
        price = (fuel_amount * 2.33) * 0.92
    else:
        price = fuel_amount * 2.33


print(f'{price:.2f} lv.')


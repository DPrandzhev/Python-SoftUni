product = input()
location = input()
amount = float(input())
price = 0

if location == "Sofia":
    if product == 'coffee':
        price = amount * 0.5
    elif product == 'water':
        price = amount * 0.8
    elif product == 'beer':
        price = amount * 1.2
    elif product == 'sweets':
        price = amount * 1.45
    elif product == 'peanuts':
        price = amount * 1.60

elif location == "Plovdiv":
    if product == 'coffee':
        price = amount * 0.4
    elif product == 'water':
        price = amount * 0.7
    elif product == 'beer':
        price = amount * 1.15
    elif product == 'sweets':
        price = amount * 1.30
    elif product == 'peanuts':
        price = amount * 1.50

elif location == "Varna":
    if product == 'coffee':
        price = amount * 0.45
    elif product == 'water':
        price = amount * 0.7
    elif product == 'beer':
        price = amount * 1.10
    elif product == 'sweets':
        price = amount * 1.35
    elif product == 'peanuts':
        price = amount * 1.55

print(price)

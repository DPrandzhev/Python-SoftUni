month = input()
amount_nights = int(input())

price_studio = 0
price_apartment = 0

#Apartament

if amount_nights <= 14:
    if month == "May" or month == "October":
        price_apartment = amount_nights * 65
    elif month == "June" or month == "September":
        price_apartment = amount_nights * 68.70
    elif month == "July" or month == "August":
        price_apartment = amount_nights * 77
elif amount_nights > 14:
    if month == "May" or month == "October":
        price_apartment = (amount_nights * 65) * 0.9
    elif month == "June" or month == "September":
        price_apartment = (amount_nights * 68.70) * 0.9
    elif month == "July" or month == "August":
        price_apartment = (amount_nights * 77) * 0.9

#Studio

if month == "May" or month == "October":
    if amount_nights <= 7:
        price_studio = amount_nights * 50
    elif amount_nights < 14:
        price_studio = (amount_nights * 50) * 0.95
    elif amount_nights > 14:
        price_studio = (amount_nights * 50) * 0.7

elif month == "June" or month == "September":
    if amount_nights > 14:
        price_studio = (amount_nights * 75.2) * 0.8
    else:
        price_studio = amount_nights * 75.2

elif month == "July" or month == "August":
    price_studio = amount_nights * 76

print(f"Apartment: {price_apartment:.2f} lv.")
print(f"Studio: {price_studio:.2f} lv.")







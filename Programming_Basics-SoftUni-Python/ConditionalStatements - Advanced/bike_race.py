#Veloklub Ogneni_Pedali
amount_junior_cyclist = int(input())
amount_senior_cyclist = int(input())
track_type = input()
# ["trail", "cross-country", "downhill", "road"]

price_jr = 0
price_sr = 0
discount = 0

if track_type == "trail":
    price_jr = 5.50
elif track_type == "cross-country":
    price_jr = 8
elif track_type == "downhill":
    price_jr = 12.25
elif track_type == "road":
    price_jr = 20

if track_type == "trail":
    price_sr = 7
elif track_type == "cross-country":
    price_sr = 9.5
elif track_type == "downhill":
    price_sr = 13.75
elif track_type == "road":
    price_sr = 21.5

total_sum = amount_junior_cyclist * price_jr + amount_senior_cyclist * price_sr
expenses = total_sum * 0.05

if track_type == "cross-country" and (amount_junior_cyclist + amount_senior_cyclist) >= 50:
    discount = (total_sum - expenses) * 0.25
else:
    pass

donated_amount = total_sum - expenses - discount

print(f"{donated_amount:.2f}")
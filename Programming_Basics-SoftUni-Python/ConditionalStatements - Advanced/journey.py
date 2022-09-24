budget = float(input())
season = input()
destination = ""
trip = ""
amount = 0

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        trip = "Camp"
        amount = budget * 0.30
    elif season == "winter":
        amount = budget * 0.70
        trip = "Hotel"

elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        amount = budget * 0.4
        trip = "Camp"
    elif season == "winter":
        amount = budget * 0.8
        trip = "Hotel"

else:
    destination = "Europe"
    amount = budget * 0.9
    trip = "Hotel"

print(f'Somewhere in {destination}')
print(f'{trip} - {amount:.2f}')
budget = float(input())
season = input()

location = ""
place_to_sleep = ""
price = 0

if budget <= 1000:
    place_to_sleep = "Camp"
    if season == "Summer":
        location = "Alaska"
        price = budget * 0.65
    elif season == "Winter":
        location = "Morocco"
        price = budget * 0.45

elif budget <= 3000:
    place_to_sleep = "Hut"
    if season == "Summer":
        location = "Alaska"
        price = budget * 0.8
    elif season == "Winter":
        location = "Morocco"
        price = budget * 0.60

elif budget > 3000:
    place_to_sleep = "Hotel"
    if season == "Summer":
        location = "Alaska"
        price = budget * 0.9
    elif season == "Winter":
        location = "Morocco"
        price = budget * 0.9

print(f'{location} - {place_to_sleep} - {price:.2f}')

season = input()
group_gender = input()
number_students = int(input())
number_nights = int(input())

sports = ""
price_total = 0
discount = 0
price_per_night = 0

if group_gender == "girls" or group_gender == "boys":
    if season == "Winter":
        price_per_night = 9.6
    elif season == "Spring":
        price_per_night = 7.2
    elif season == "Summer":
        price_per_night = 15

elif group_gender == "mixed":
    if season == "Winter":
        price_per_night = 10
    elif season == "Spring":
        price_per_night = 9.5
    elif season == "Summer":
        price_per_night = 20

if group_gender == "girls":
    if season == "Winter":
        sports = "Gymnastics"

    elif season == "Spring":
        sports = "Athletics"

    elif season == "Summer":
        sports = "Volleyball"

elif group_gender == "boys":
    if season == "Winter":
        sports = "Judo"

    elif season == "Spring":
        sports = "Tennis"

    elif season == "Summer":
        sports = "Football"

elif group_gender == "mixed":
    if season == "Winter":
        sports = "Ski"

    elif season == "Spring":
        sports = "Cycling"

    elif season == "Summer":
        sports = "Swimming"


if number_students >= 50:
    price_per_night = price_per_night * 0.5
elif 20 <= number_students < 50:
    price_per_night = price_per_night * 0.85
elif 10 <= number_students < 20:
    price_per_night = price_per_night * 0.95


price_total = (number_students * number_nights * price_per_night) - discount

print(f'{sports} {price_total:.2f} lv.')
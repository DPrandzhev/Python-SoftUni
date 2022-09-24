# from math import floor, ceil
import math


loze_square_m = int(input())
grapes_per_m = float(input())
required_litre_wine = int(input())
workers = int(input())

total_grapes = loze_square_m * grapes_per_m
wine = (0.4 * total_grapes) / 2.5

diff = abs(wine - required_litre_wine)
liters_per_person = diff / workers


if wine >= required_litre_wine:
    print(f"Good harvest this year! Total wine: {math.floor(wine)} liters.")
    print(f'{math.ceil(diff)} liters left -> {math.ceil(liters_per_person)} liters per person.')


else:
    print(f"It will be a tough winter! More {math.floor(diff)} liters wine needed.")

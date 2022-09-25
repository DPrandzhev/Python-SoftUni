# from math import floor, ceil
#
#
# number_km = int(input())
# time_of_day = input()
#
# price_taxi_day = 0.7 + (0.79 * number_km)
# price_taxi_night = 0.7 + (0.90 * number_km)
#
# price_bus = 0.09 * number_km
# #min km - 20
#
# price_train = 0.06 * number_km
# #min km - 100
#
# if number_km < 20:
#     if time_of_day == "day":
#         print(f"{price_taxi_day:.2f}")
#     elif time_of_day == "night":
#         print(f"{price_taxi_night:.2f}")
# elif number_km < 100:
#     print(f"{price_bus:.2f}")
# else:
#     print(f"{price_train:.2f}")
#


from math import floor, ceil


number_km = int(input())
time_of_day = input()

if number_km < 20:
    if time_of_day == "day":
        price_taxi_day = 0.7 + (0.79 * number_km)
        print(f"{price_taxi_day:.2f}")
    elif time_of_day == "night":
        price_taxi_night = 0.7 + (0.90 * number_km)
        print(f"{price_taxi_night:.2f}")
elif number_km < 100:
    price_bus = 0.09 * number_km
    print(f"{price_bus:.2f}")
else:
    print(f"{price_train:.2f}")
    price_train = 0.06 * number_km















if abc = 1:
    if bca = 1:
        if bba = 1
            pass
        elif aaa = 1
            continue
    elif bbbassd == 1
    pass
else:
    this
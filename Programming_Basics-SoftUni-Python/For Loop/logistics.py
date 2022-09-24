number_of_loads = int(input())

price_bus = 0
price_truck = 0
price_train = 0

weight_sum = 0

#percent loads variables
p1_loads = 0
p2_loads = 0
p3_loads = 0

for i in range(1, number_of_loads + 1):
    weight_in_tons = int(input())

    if weight_in_tons <= 3:
        # vehicle = "microbus"
        price_bus += 200 * weight_in_tons
        p1_loads += weight_in_tons
    elif weight_in_tons <= 11:
        # vehicle = "truck"
        price_truck += 175 * weight_in_tons
        p2_loads += weight_in_tons

    else:
        # vehicle = "train"
        price_train += 120 * weight_in_tons
        p3_loads += weight_in_tons

    weight_sum += weight_in_tons

avg_price_total = (price_bus + price_truck + price_train) / weight_sum
avg_price_bus = p1_loads / weight_sum * 100
avg_price_truck = p2_loads / weight_sum * 100
avg_price_train = p3_loads / weight_sum * 100


print(f" {avg_price_total:.2f}")
print(f" {avg_price_bus:.2f}%")
print(f" {avg_price_truck:.2f}%")
print(f" {avg_price_train:.2f}%")


# count_cargo = int(input())
# total_weight_cargo = 0
# tons_by_bus = 0
# tons_by_truck = 0
# tons_by_train = 0
#
# for cargo in range(1, count_cargo + 1):
#     weight_cargo = int(input())
#     total_weight_cargo += weight_cargo
#     if weight_cargo <= 3:
#         tons_by_bus += weight_cargo
#         price_bus = 200 * tons_by_bus
#     elif weight_cargo <= 11:
#         tons_by_truck += weight_cargo
#         price_truck = 175 * tons_by_truck
#     else:
#         tons_by_train += weight_cargo
#         price_train = 120 * tons_by_train
#
# average_price_ton = (price_bus + price_truck + price_train) / total_weight_cargo
# print(f"{average_price_ton:.2f}")
# percent_bus = tons_by_bus / total_weight_cargo * 100
# print(f"{percent_bus:.2f}%")
# percent_truck = tons_by_truck / total_weight_cargo * 100
# print(f"{percent_truck:.2f}%")
# percent_train = tons_by_train / total_weight_cargo * 100
# print(f"{percent_train:.2f}%")
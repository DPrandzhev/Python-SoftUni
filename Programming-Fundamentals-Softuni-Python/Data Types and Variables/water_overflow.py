number_of_lines = int(input())
capacity = 0

for litres in range(number_of_lines):
    litres_of_water = int(input())
    capacity += litres_of_water

    if capacity >= 255:
        capacity -= litres_of_water
        print("Insufficient capacity!")
        continue

print(capacity)
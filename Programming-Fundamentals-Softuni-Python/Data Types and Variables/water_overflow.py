number_of_lines = int(input())
max_capacity = 255
current_capacity = 0

for litres in range(number_of_lines):
    litres_of_water = int(input())
    current_capacity += litres_of_water

    if current_capacity >= max_capacity:
        current_capacity -= litres_of_water
        print("Insufficient capacity!")
        continue

print(current_capacity)
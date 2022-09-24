quantity_of_decorations = int(input())
days_until_christmas = int(input())
spirit = 0
total_spent = 0

ornament_set = 2
tree_skirt = 5
tree_garland = 3
tree_lights = 15


for days in range(1, days_until_christmas +1):
    if days % 11 == 0:
        quantity_of_decorations += 2

    if days % 2 == 0:
        total_spent += quantity_of_decorations * ornament_set
        spirit += 5

    if days % 3 == 0:
        total_spent += quantity_of_decorations * tree_skirt
        total_spent += quantity_of_decorations * tree_garland
        spirit += 13

    if days % 5 == 0:
        total_spent += quantity_of_decorations * tree_lights
        spirit += 17
        if days % 3 == 0:
            spirit += 30
    if days % 10 == 0:
        spirit -= 20
        total_spent += tree_skirt + tree_garland + tree_lights

if days_until_christmas % 10 == 0:
    spirit -= 30

print(f"Total cost: {total_spent}")
print(f"Total spirit: {spirit}")
from math import floor

group_size = int(input())
days_input = int(input())
coins = 0
for days in range(1, days_input + 1):
    if days % 10 == 0:
        group_size -= 2
    if days % 15 == 0:
        group_size += 5

    if days % 3 == 0:
        coins -= group_size * 3
    if days % 5 == 0:
        coins += group_size * 20
        if days % 3 == 0:
            coins -= group_size * 2


    coins += 50
    coins -= 2 * group_size

coins_each = int(coins / group_size)

print(f"{group_size} companions received {coins_each} coins each.")

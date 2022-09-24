cargo_space = float(input())
command = input()
is_full = False
suitcase_counter = 0
used_cargo = 0

while command != "End":
    suitcase_volume = float(command)
    suitcase_counter += 1

    if suitcase_counter % 3 == 0:
        suitcase_volume += suitcase_volume * 0.1

    used_cargo += suitcase_volume

    if used_cargo > cargo_space:
        is_full = True
        suitcase_counter -= 1
        break


    command = input()

if is_full:
    print("No more space!")
    print(f"Statistic: {suitcase_counter} suitcases loaded.")
else:
    print("Congratulations! All suitcases are loaded!")
    print(f"Statistic: {suitcase_counter} suitcases loaded.")
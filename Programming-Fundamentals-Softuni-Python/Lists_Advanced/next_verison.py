
def verison_changer(one, two, three):

    if three != 9:
        three += 1

    elif two == 9 and three == 9:
        three = 0
        two = 0
        one += 1

    elif three == 9:
        three = 0
        two += 1

    return [one, two, three]


current_verison = list(map(int, input().split('.')))

result = verison_changer(current_verison[0], current_verison[1], current_verison[2])
formated_result = str(result)
print(f"{result[0]}.{result[1]}.{result[2]}")

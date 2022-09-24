number_of_strings = int(input())
list_n = []
for st in range(1, number_of_strings + 1):
    string = input()
    ascii_value = []
    for character in string:
        ascii_value.append(ord(character))

    list_n = ascii_value
    if 46 in list_n or 44 in list_n or 95 in list_n:
        print(f"{string} is not pure!")
    else:
        print(f"{string} is pure.")

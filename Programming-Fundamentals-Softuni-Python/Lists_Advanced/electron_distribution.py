number_of_electrons = int(input())
position = 0
lst_shells = []
while True:
    if number_of_electrons == 0:
        break

    position += 1
    shell = 2 * position ** 2

    if number_of_electrons >= shell:
        lst_shells.append(shell)
        number_of_electrons -= shell
    else:
        lst_shells.append(number_of_electrons)
        number_of_electrons = 0

print(lst_shells)
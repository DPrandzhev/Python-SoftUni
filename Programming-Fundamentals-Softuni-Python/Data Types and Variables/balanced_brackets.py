number_of_lines = int(input())
brackets = 0

for i in range(number_of_lines):
    command = input()
    if command == "(":
        brackets += 1
    elif command == ")":
        brackets -= 1
    else:
        continue

    if brackets != 0 and brackets != 1:
        print("UNBALANCED")
        break
else:
    print("BALANCED")
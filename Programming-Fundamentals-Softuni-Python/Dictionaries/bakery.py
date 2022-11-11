line_input = input().split()
bakery = {}

for value in range(0, len(line_input), 2):
    key = line_input[value]
    value = line_input[value + 1]
    bakery[key] = int(value)

print(bakery)



line_input = input().split()
products = input().split()
bakery = {}

for value in range(0, len(line_input), 2):
    key = line_input[value]
    value = line_input[value + 1]
    bakery[key] = int(value)

for item in products:
    if item in bakery:
        print(f"We have {bakery[item]} of {item} left")
    else:
        print(f"Sorry, we don't have {item}")


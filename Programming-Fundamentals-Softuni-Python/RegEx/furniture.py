import re
input_string = input()
false = True
bought = []
total_sum = 0
pattern = r'>>([A-Za-z]+)<<(\d+\.?\d*)!(\d+)'

while false:

    if input_string == "Purchase":
        break

    match = re.search(pattern, input_string)
    if match:
        furniture, price, amount = match.groups()
        bought.append(furniture)
        total_sum += int(amount) * float(price)

    input_string = input()

print("Bought furniture:")
for item in bought:
    print(item)
print(f"Total money spend: {total_sum:.2f}")
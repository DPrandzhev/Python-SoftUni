command = input()
print_receipt = False
price_without_tax = 0
total_price = 0

while True:
    if command == "special" or command == "regular":
        break

    current_command = float(command)

    if current_command <= 0:
        print("Invalid price!")
        pass
    else:
        price_without_tax += current_command


    command = input()



if command == "special":
    total_price = total_price * 0.9

if price_without_tax > 0:
    tax = price_without_tax * 0.2
    total_price = price_without_tax + tax
    if command == "special":
        total_price = total_price * 0.9

    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {price_without_tax:.2f}$")
    print(f"Taxes: {tax:.2f}$")
    print("-----------")
    print(f"Total price: {total_price:.2f}$")

else:
    print("Invalid order!")


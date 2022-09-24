number_of_orders = int(input())
price_total = 0
price = 0
for _ in range(1, number_of_orders + 1):
    price_per_capsule = float(input())
    days = int(input())
    capsule_needed_per_day = int(input())
    if price_per_capsule < 0.01 or price_per_capsule > 100:
        continue
    elif days < 1 or days > 31:
        continue
    elif capsule_needed_per_day < 1 or capsule_needed_per_day > 2000:
        continue

    price = price_per_capsule * days * capsule_needed_per_day
    price_total += price
    print(f"The price for the coffee is: ${price:.2f}")

print(f"Total: ${price_total:.2f}")

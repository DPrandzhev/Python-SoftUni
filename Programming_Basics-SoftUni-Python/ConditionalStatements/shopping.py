budget = float(input())
number_vga = int(input())
number_cpu = int(input())
number_ram = int(input())
discount = 0

price_vga = 250 * number_vga
price_cpu = price_vga * 0.35
price_ram = price_vga * 0.1

total_sum = price_vga + number_cpu * price_cpu + number_ram * price_ram

if number_vga > number_cpu:
    discount = total_sum * 0.15
else:
    pass

diff = abs(total_sum - discount - budget)


if budget < total_sum:
    print(f"Not enough money! You need {diff:.2f} leva more!")

else:
    print(f"You have {diff:.2f} leva left!")







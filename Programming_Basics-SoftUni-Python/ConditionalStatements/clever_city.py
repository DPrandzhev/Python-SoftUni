age_lilly = int(input())
price_machine = float(input())
price_toy = int(input())

money_pool = 0
money = 0
count_toys = 0
reket = 0
for i in range(1, age_lilly + 1):
    if i % 2 == 0:
        reket += 1
        money_pool += money
        money += 10
    else:
        count_toys = count_toys + 1

sum = money_pool + money

result = sum + (count_toys * price_toy) - reket

diff = abs(result - price_machine)

if result >= price_machine:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")
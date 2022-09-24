# •	Магнолии – 3.25 лева
# •	Зюмбюли – 4 лева
# •	Рози – 3.50 лева
# •	Кактуси – 8 лева

# 5 % danak
from math import ceil, floor

magnolia = int(input())
zumbul = int(input())
roses = int(input())
cactus = int(input())
gift = float(input())

total_net_amount = magnolia * 3.25 + zumbul * 4 + roses * 3.5 + cactus * 8
tax = total_net_amount * 0.05
total_brute_amount = total_net_amount - tax

diff = abs(total_brute_amount - gift)

if total_brute_amount < gift:
    print(f" She will have to borrow {ceil(diff)} leva.")
elif total_brute_amount >= gift:
    print(f"She is left with {floor(diff)} leva.")
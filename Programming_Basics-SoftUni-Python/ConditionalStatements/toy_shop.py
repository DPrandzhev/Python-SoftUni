price_trip = float(input())
number_puzzles = int(input())
number_dolls = int(input())
number_bears = int(input())
number_minions = int(input())
number_trucks = int(input())
discount = 0


total_sum = number_puzzles * 2.60 + number_dolls * 3 + number_bears * 4.1 + number_minions * 8.2 + number_trucks * 2
number_toys_total = number_minions + number_bears + number_dolls + number_puzzles + number_trucks


if number_toys_total >= 50:
    discount = total_sum * 0.25
else:
    number_toys_total <= 49
    discount = 0

customer_price = total_sum - discount
rent = customer_price * 0.1

profit = customer_price - rent

if profit >= price_trip:
    print (f"Yes! {profit - price_trip:.2f} lv left.")
else:
    print (f"Not enough money! {price_trip - profit:.2f} lv needed.")

# Петя има магазин за детски играчки. Тя получава голяма поръчка, която трябва да изпълни. С парите, които ще спечели иска да отиде на екскурзия.
# Цени на играчките:
# •	Пъзел - 2.60 лв.
# •	Говореща кукла - 3 лв.
# •	Плюшено мече - 4.10 лв.
# •	Миньон - 8.20 лв.
# •	Камионче - 2 лв.
# Ако поръчаните играчки са 50 или повече магазинът прави отстъпка 25% от общата цена. От спечелените пари Петя трябва да даде 10% за наема на магазина. Да се пресметне дали парите ще ѝ стигнат да отиде на екскурзия.

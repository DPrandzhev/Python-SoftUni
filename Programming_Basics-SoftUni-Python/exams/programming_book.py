price_per_page = float(input())
price_per_cover = float(input())
discount_percent = int(input())
designer_cost = float(input())
percent_paid_by_ppl = int(input())

starting_cost = (price_per_page * 899) + (price_per_cover * 2)
discounted_amount = starting_cost * (discount_percent / 100)
discounted_cost = starting_cost - discounted_amount

total_sum = discounted_cost + designer_cost

avtonom_percent = total_sum * (percent_paid_by_ppl / 100)
avtonom_price = total_sum - avtonom_percent


print(f"Avtonom should pay {avtonom_price:.2f} BGN.")
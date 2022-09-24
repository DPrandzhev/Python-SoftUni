import math

needed_processors = int(input())
number_employees = int(input())
working_days = int(input())

price_processor = 110.10

total_hours = number_employees * working_days * 8
processors_made = math.floor(total_hours / 3)

diff = abs(needed_processors - processors_made)
diff_cost = diff * price_processor
if processors_made < needed_processors:
    print(f"Losses: -> {diff_cost:.2f} BGN")
else:
    print(f"Profit: -> {diff_cost:.2f} BGN")
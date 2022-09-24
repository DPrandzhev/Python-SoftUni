number_of_locations = int(input())

gold_collected = 0
for i in range(1, number_of_locations + 1):
    expected_avg_amount = float(input())
    days_to_dig = int(input())
    for j in range(1, days_to_dig + 1):
        amount_of_gold = float(input())
        gold_collected += amount_of_gold

    avg_gold_per_location = gold_collected / days_to_dig
    diff = abs(avg_gold_per_location - expected_avg_amount)
    if avg_gold_per_location >= expected_avg_amount:
        print(f"Good job! Average gold per day: {avg_gold_per_location:.2f}.")
    else:
        print(f"You need {diff:.2f} gold.")
    gold_collected = 0
season = input()
km_per_month = float(input())


money_talks = 0

if km_per_month <= 5000:
    if season == "Spring" or season == "Autumn":
        money_talks = km_per_month * 0.75 * 4
    elif season == "Summer":
        money_talks = km_per_month * 0.9 * 4
    elif season == "Winter":
        money_talks = km_per_month * 1.05 * 4

elif 5000 < km_per_month <= 10000:
    if season == "Spring" or season == "Autumn":
        money_talks = km_per_month * 0.95 * 4
    elif season == "Summer":
        money_talks = km_per_month * 1.1 * 4
    elif season == "Winter":
        money_talks = km_per_month * 1.25 * 4
elif 10000 < km_per_month <= 20000:
    money_talks = km_per_month * 1.45 * 4

money_gross = money_talks * 0.9

print(f'{money_gross:.2f}')
deposit = float(input())
months = int(input())
year = float(input())

interest = deposit * (year / 100)
interest_one_month = interest / 12
total = deposit + months * interest_one_month

print(deposit + months * interest_one_month)
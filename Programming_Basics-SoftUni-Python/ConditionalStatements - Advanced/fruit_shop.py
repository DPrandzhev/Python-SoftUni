fruit = input()
day = input()
amount = float(input())
price = 0

# if day != "Saturday" and day != "Sunday":
if day == "Monday" or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday':
    if fruit == "banana":
        price = amount * 2.50
    elif fruit == "apple":
        price = amount * 1.20
    elif fruit == "orange":
        price = amount * 0.85
    elif fruit == "grapefruit":
        price = amount * 1.45
    elif fruit == "kiwi":
        price = amount * 2.70
    elif fruit == "pineapple":
        price = amount * 5.50
    elif fruit == "grapes":
        price = amount * 3.85
elif day == 'Saturday' or day == 'Sunday':
    if fruit == "banana":
        price = amount * 2.7
    elif fruit == "apple":
        price = amount * 1.25
    elif fruit == "orange":
        price = amount * 0.90
    elif fruit == "grapefruit":
        price = amount * 1.60
    elif fruit == "kiwi":
        price = amount * 3
    elif fruit == "pineapple":
        price = amount * 5.60
    elif fruit == "grapes":
        price = amount * 4.20
    else:
        print('error')

if price == 0:
    print('error')

else:
    print(f'{price:.2f}')

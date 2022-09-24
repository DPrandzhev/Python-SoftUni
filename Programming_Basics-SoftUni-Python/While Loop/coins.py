coin_input = float(input())

coin_counter = 0
coin_total = round(coin_input * 100)

while coin_total != 0:

    if coin_total >= 200:
        coin_counter += 1
        coin_total -= 200
    elif coin_total >= 100:
        coin_counter += 1
        coin_total -= 100
    elif coin_total >= 50:
        coin_counter += 1
        coin_total -= 50
    elif coin_total >= 20:
        coin_counter += 1
        coin_total -= 20
    elif coin_total >= 10:
        coin_counter += 1
        coin_total -= 10
    elif coin_total >= 5:
        coin_counter += 1
        coin_total -= 5
    elif coin_total >= 2:
        coin_counter += 1
        coin_total -= 2
    elif coin_total >= 1:
        coin_counter += 1
        coin_total -= 1

print(coin_counter)
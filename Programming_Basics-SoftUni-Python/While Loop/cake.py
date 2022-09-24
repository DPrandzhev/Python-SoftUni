cake_widith = int(input())
cake_height = int(input())

cake_size = cake_widith * cake_height
pieces_takes = input()
no_cake = False

while pieces_takes != "STOP":
    cake_takes = int(pieces_takes)
    cake_size -= cake_takes

    if cake_size <= 0:
        no_cake = True
        break

    pieces_takes = input()

# diff = abs(cake_size - cake_takes)
if no_cake:
    print(f"No more cake left! You need {abs(cake_size)} pieces more.")
else:
    print(f"{cake_size} pieces are left.")
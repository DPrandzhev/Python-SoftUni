number_n = int(input())
is_reached = True
conter_strike = 0
for a in range(1, 9 + 1):
    for b in range(9, a, -1):
        for c in range(0, 9 + 1):
            for d in range(9, c, -1):
                sum_abcd = a + b + c + d
                multip_abcd = a * b * c * d
                if sum_abcd == multip_abcd and number_n % 10 == 5:
                    print(f'{a}{b}{c}{d}')
                    is_reached = False
                    break
                elif multip_abcd // sum_abcd == 3 and number_n % 3 == 0:
                    print(f'{d}{c}{b}{a}')
                    is_reached = False
                    break
                break
            break
        break
if is_reached:
    print("Nothing found")

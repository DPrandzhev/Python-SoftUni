price_skumriya = float(input())
price_caca = float(input())
amount_palamud = float(input())
amount_safrid = float(input())
amount_midi = int(input())

price_palamud = price_skumriya + (price_skumriya * 0.60)
price_safrid = price_caca + (price_caca * 0.8)
price_midi = 7.50

total_sum = amount_palamud * price_palamud + amount_safrid * price_safrid + amount_midi * price_midi
print(f'{total_sum:.2f}')

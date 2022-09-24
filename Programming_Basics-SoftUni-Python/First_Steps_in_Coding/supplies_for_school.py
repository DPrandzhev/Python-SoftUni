prices_pens = 5.80
prices_markers = 7.20
prices_solution = 1.20

pens = int(input())
markers = int(input())
solution = int(input())
discount = int(input())

price = pens * prices_pens + markers * prices_markers + solution * prices_solution
discount = price * (discount / 100)

print(price - discount)

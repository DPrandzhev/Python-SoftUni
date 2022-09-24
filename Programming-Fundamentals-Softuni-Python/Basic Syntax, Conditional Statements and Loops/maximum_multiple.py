divisor = int(input())
boundary = int(input())

for n in range(boundary, divisor, -1):
    if n % divisor == 0 and boundary >= n > 0:
        break

print(n)
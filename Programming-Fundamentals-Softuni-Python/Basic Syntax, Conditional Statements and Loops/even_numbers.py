number_n = int(input())
is_odd = False

for _ in range(number_n):
    number = int(input())
    if not number % 2 == 0:
        print(f"{number} is odd!")
        break

else:
    print("All numbers are even.")

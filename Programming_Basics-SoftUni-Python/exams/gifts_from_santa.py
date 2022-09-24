numbers_n = int(input())
number_m = int(input())
number_s = int(input())

for adress in range(number_m, numbers_n - 1, -1):
    # if 0 <= numbers_n < number_m and numbers_n < number_m <= 10000 and numbers_n <= number_s <= number_m:

        if adress % 2 == 0 and adress % 3 == 0:
            if adress == number_s:
                break


            print(adress, end=" ")

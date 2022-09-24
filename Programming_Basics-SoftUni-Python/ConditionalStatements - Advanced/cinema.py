movie = input()
rows_r = int(input())
columns_c = int(input())
income = 0

cinema_capacity = rows_r * columns_c

if movie == 'Premiere':
    income = cinema_capacity * 12
elif movie == 'Normal':
    income = cinema_capacity * 7.50
elif movie == 'Discount':
    income = cinema_capacity * 5


print(f'{income:.2f} leva')
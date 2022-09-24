# Пример: 20 почивни дни -> работните дни са 345 (365 – 20 = 345).
# Реалното време за игра е 24 275 минути (345 * 63 + 20 *127).
# Разликата от нормата е 5 725 минути (30 000 – 24 275 = 5 725) или 95 часа и 25 минути.

# PTO - paid time off
number_PTO = int(input())

play_days = number_PTO * 127
regular_days = (365 - number_PTO) * 63

time_sum = play_days + regular_days
sleep_treshold = 30000

time = abs(sleep_treshold - time_sum)

h = time // 60
m = time % 60


if sleep_treshold < time_sum:
    print ("Tom will run away")
    print(f' {h} hours and {m} minutes more for play')

else:
    print("Tom sleeps well")
    print(f' {h} hours and {m} minutes less for play')

from math import ceil

series_name = input()
epizode_lenght = int(input())
lunch_break = int(input())

time_for_lunch = lunch_break * 0.125
time_to_rest = lunch_break * 0.25


remaining_time = lunch_break - time_to_rest - time_for_lunch
diff = abs(epizode_lenght - remaining_time)
diff = ceil(diff)


if remaining_time >= epizode_lenght:
    print(f"You have enough time to watch {series_name} and left with {diff} minutes free time.")
else:
    print(f"You don't have enough time to watch {series_name}, you need {diff} more minutes.")
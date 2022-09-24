from math import floor
current_record = float(input())
distance = float(input())
meters_per_second = float(input())



extra_time = floor((distance // 50) * 30)

time_needed = (distance * meters_per_second) + extra_time

if time_needed < current_record:
    print(f"Yes! The new record is {time_needed:.2f} seconds.")
else:
    print(f"No! He was {(time_needed - current_record):.2f} seconds slower.")


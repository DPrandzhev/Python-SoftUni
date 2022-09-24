current_record = float(input())
distance_meters = float(input())
time_seconds = float(input())


extra_time = (distance_meters // 15) * 12.5

time_needed = (distance_meters * time_seconds) + extra_time

if time_needed < current_record:
    print(f"Yes, he succeeded! The new world record is {time_needed:.2f} seconds.")
else:
    print(f"No, he failed! He was {(time_needed - current_record):.2f} seconds slower.")

# if time_needed >= current_record:
#     print(f"No, he failed! He was {(time_needed - current_record):.2f} seconds slower.")
# else:
#     print(f"Yes, he succeeded! The new world record is {time_needed:.2f} seconds.")

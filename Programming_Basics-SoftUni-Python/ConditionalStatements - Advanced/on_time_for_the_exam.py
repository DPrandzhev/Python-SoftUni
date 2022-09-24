exam_hour = int(input())
exam_minute = int(input())
arrive_hour = int(input())
arrive_minute = int(input())

exam_total_time = exam_hour * 60 + exam_minute
arrive_total_time = arrive_hour * 60 + arrive_minute

time_diff = abs(exam_total_time - arrive_total_time)


if arrive_total_time > exam_total_time:
    print("Late")
    if time_diff >= 60:
        hour = time_diff // 60
        minutes = time_diff % 60
        print(f" {hour}:{minutes:02d} hours after the start")
    else:
        print(f" {time_diff} minutes after the start")
elif arrive_total_time == exam_total_time or time_diff <= 30:
    print("On time")
    if time_diff >= 1:
        print(f"{time_diff} minutes before the start")

else:
    print("Early")
    if time_diff >= 60:
        hour = time_diff // 60
        minutes = time_diff % 60
        print(f" {hour}:{minutes:02d} hours before the start")
    else:
        print(f"{time_diff} minutes before the start")





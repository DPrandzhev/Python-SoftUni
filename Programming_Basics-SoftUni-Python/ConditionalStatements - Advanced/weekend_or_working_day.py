day_of_week = input()

work_days_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
if day_of_week == work_days_list:
    print("Working day")
elif day_of_week == "Saturday" or \
        day_of_week == "Sunday":
    print("Weekend")
else:
    print("Error")

from math import ceil

working_hours = input()

while working_hours != "stop":

    working_hours = float(working_hours)

    hours_to_minutes = working_hours * 60
    logged_in_hours = hours_to_minutes * 0.33

    hours = logged_in_hours // 60
    minutes = logged_in_hours % 60

    if hours == 0:
        print(f"To meet 33% for {working_hours} hour shift your OTP is: {ceil(minutes)} minutes")
    else:
        print(f"To meet 33% for {working_hours} hour shift your OTP is: {hours:.0f} hours and {ceil(minutes)} minutes")

    working_hours = input()
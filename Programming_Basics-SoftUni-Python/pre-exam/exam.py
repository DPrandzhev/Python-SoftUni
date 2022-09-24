amount_of_students = int(input())

top_students = 0
up_average = 0
down_average = 0
fail = 0
total_avg = 0

for student in range(amount_of_students):
    result = float(input())

    total_avg += result

    if result < 3:
        fail += 1
    elif result <= 3.99:
        down_average += 1
    elif result <= 4.99:
        up_average += 1
    else:
        top_students += 1


percent_top = (top_students / amount_of_students) * 100
percent_up = (up_average / amount_of_students) * 100
percent_down = (down_average / amount_of_students) * 100
percent_fail = (fail / amount_of_students) * 100

total_avg_class = total_avg / amount_of_students

print(f"Top students: {percent_top:.2f}%")
print(f"Between 4.00 and 4.99: {percent_up:.2f}%")
print(f"Between 3.00 and 3.99: {percent_down:.2f}%")
print(f"Fail: {percent_fail:.2f}%")
print(f"Average: {total_avg_class:.2f}")
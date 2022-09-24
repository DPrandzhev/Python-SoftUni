student = input()
current_class = 1
failed_class = 0
total_grade = 0
is_excluded = False

while current_class <= 12:
    year_grade = float(input())
    if year_grade < 4:
        failed_class += 1
        if failed_class == 2:
            is_excluded = True
            break
    elif year_grade <= 6:
        current_class += 1
        total_grade += year_grade

if is_excluded:
    print(f"{student} has been excluded at {current_class} grade")
else:
    avg_grade = total_grade / 12
    print(f"{student} graduated. Average grade: {avg_grade:.2f}")
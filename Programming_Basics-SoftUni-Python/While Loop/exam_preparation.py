poor_marks = int(input())

sum_grades = 0
count_grades = 0
count_poor_grades = 0
is_exluded = False

input_line = input()
while input_line != "Enough":
    grade = int(input())

    if grade <= 4:
        count_poor_grades += 1
        if count_poor_grades == poor_marks:
            is_exluded = True
            break

    sum_grades += grade
    count_grades += 1

    last_problem = input_line
    input_line = input()

avg_grade = sum_grades / count_grades

if is_exluded:
    print(f"You need a break, {count_poor_grades} poor grades.")
else:
    print(f"Average score: {avg_grade:.2f}")
    print(f"Number of problems: {count_grades}")
    print(f"Last problem: {last_problem}")

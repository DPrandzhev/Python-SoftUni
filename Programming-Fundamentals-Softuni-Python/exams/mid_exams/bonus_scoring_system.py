
from math import ceil as cl
number_of_students = int(input())
total_number_lectures = int(input())
aditional_bonus = int(input())

total_bonus = 0
max_bonus = 0
attended_lectures = 0


for att in range(1, number_of_students + 1):
    student_attendances = int(input())
    total_bonus = student_attendances / total_number_lectures * (5 + aditional_bonus)
    if total_bonus > max_bonus:
        max_bonus = total_bonus
        attended_lectures = student_attendances

print(f"Max Bonus: {cl(max_bonus)}.")
print(f"The student has attended {attended_lectures} lectures.")
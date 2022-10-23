first_employee_efficency = int(input())
second_employee_efficency = int(input())
third_employee_efficency = int(input())
students_count = int(input())
hours_needed = 0
is_served = False

all_employee_efficiency = first_employee_efficency + second_employee_efficency + third_employee_efficency

while students_count > 0:
    hours_needed += 1
    if hours_needed % 4 != 0:
        students_count -= all_employee_efficiency


print(f"Time needed: {hours_needed}h.")
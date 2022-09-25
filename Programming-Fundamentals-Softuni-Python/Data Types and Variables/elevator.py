number_of_people = int(input())
capacity_p = int(input())
course = 0
if capacity_p > 0:
    for i in range(1, number_of_people + 1):
        if number_of_people <= 0:
            break
        course += 1
        number_of_people -= capacity_p

print(course)
dict = {}
command = input().split(":")
while len(command) > 1:
    name, id, course = command[0], command[1], command[2]
    if course not in dict:
        dict[course] = []

    dict[course].append(f"{name} - {id}")

    command = input().split(":")
searched_course = command[0].replace("_", " ")
for student in dict[searched_course]:
    print(student)

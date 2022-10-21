to_do = []

while True:
    command = input()
    if command == "End":
        break

    priority_level, task = command.split("-")
    priority_level = int(priority_level)
    to_do.append((priority_level, task))

# sorted_list = [task_data[1] for task_data in sorted(to_do)]

sorted_list = []
for data in sorted(to_do):
    sorted_list.append(data[1])

print(sorted_list)
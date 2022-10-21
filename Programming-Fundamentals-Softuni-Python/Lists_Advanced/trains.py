number_of_wagons = int(input())
lst_train = []

for _ in range(number_of_wagons):
    lst_train.append(0)

while True:
    command = input()

    if command == "End":
        break

    split_command = command.split(' ')

    if split_command[0] == "add":
        lst_train[-1] += int(split_command[1])

    elif split_command[0] == "insert":
        index = int(split_command[1])
        people = int(split_command[2])
        lst_train[index] += people

    elif split_command[0] == "leave":
        index = int(split_command[1])
        people = int(split_command[2])
        lst_train[index] -= people

print(lst_train)
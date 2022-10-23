original_array = list(map(int, input().split()))
modified_array = original_array

command = input()
while command != "end":

    if command == "decrease":
        modified_array = [x - 1 for x in modified_array]
        command = input()
        continue

    action, index_one, index_two = [x if x.isalpha() else int(x) for x in command.split()]


    if action == "swap":
        modified_array[index_one], modified_array[index_two] = modified_array[index_two], modified_array[index_one]

    elif action == "multiply":
        modified_array[index_one] *= modified_array[index_two]

    command = input()


print(*modified_array, sep=", ")

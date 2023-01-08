the_string = input()
command = input()
false = True
removed_chars = []
while false:
    if command == "Done":
        break

    current = command.split(' ')
    if current[0] == 'Change':
        substring = current[1]
        replacement = current[2]
        the_string = the_string.replace(substring, replacement)
        print(the_string)

    elif current[0] == 'Includes':
        substring = current[1]
        if substring in the_string:
            print('True')
        elif substring not in the_string:
            print('False')

    elif 'End' == current[0]:
        substring = current[1]
        if the_string.endswith(substring):
            print('True')
        else:
            print('False')

    elif current[0] == 'Uppercase':
        the_string = the_string.upper()
        print(the_string)

    elif current[0] == 'FindIndex':
        char = current[1]
        index = the_string.find(char)
        print(index)

    elif current[0] == 'Cut':
        start_index, count = int(current[1]), int(current[2])
        removed_chars = the_string[start_index:] + the_string[:count]
        print(removed_chars[:count])

    command = input()

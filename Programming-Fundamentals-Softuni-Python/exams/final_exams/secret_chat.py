concealed_message = input()

command = input()
false = True

while True:
    if command == "Reveal":
        break
    error = False
    current_command = command.split(':|:')

    if current_command[0] == "ChangeAll":
        substring = current_command[1]
        replacement = current_command[2]

        concealed_message = concealed_message.replace(substring, replacement)

    elif current_command[0] == "Reverse":
        substring = current_command[1]
        if substring in concealed_message:
            index = concealed_message.index(substring)
            lenght = len(substring)
            for msg in range(lenght):
                concealed_message = concealed_message[:index] + concealed_message[index + 1:]
            concealed_message += substring[::-1]

        else:
            error = True
            print("error")

    elif current_command[0] == 'InsertSpace':
        index = int(current_command[1])
        concealed_message = concealed_message[:index] + ' ' + concealed_message[index:]

    if not error:
        print(concealed_message)

    command = input()

print(f'You have a new text message: {concealed_message}')


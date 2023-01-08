decrypted_message = input()
command = input()
false = True

while false:

    if command == "Decode":
        break

    current_command = command.split('|')

    if current_command[0] == "Move":
        number_of_letters = int(current_command[1])
        for i in range(number_of_letters):
            decrypted_message = decrypted_message[1:] + decrypted_message[0]

    elif current_command[0] == "Insert":
        index = int(current_command[1])
        value = current_command[2]
        decrypted_message = decrypted_message[:index] + value + decrypted_message[index:]

    elif current_command[0] == "ChangeAll":
        substring = current_command[1]
        replacement = current_command[2]

        decrypted_message = decrypted_message.replace(substring, replacement)

    command = input()

print(f'The decrypted message is: {decrypted_message}')
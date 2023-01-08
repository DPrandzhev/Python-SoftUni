raw_key = input()

command = input()
false = True

while false:
    if command == 'Generate':
        print(f'Your activation key is: {raw_key}')
        break
    current = command.split('>>>')

    if current[0] == 'Contains':
        substring = current[1]
        if substring in raw_key:
            print(f"{raw_key} contains {substring}")
        else:
            print("Substring not found!")

    elif current[0] == 'Flip':
        up_low = current[1]
        start_index, end_index = int(current[2]), int(current[3])
        if up_low == "Upper":
            raw_key = raw_key[:start_index] + raw_key[start_index:end_index].upper() + raw_key[end_index:]
            print(f"{raw_key}")
        elif up_low == "Lower":
            raw_key = raw_key[:start_index] + raw_key[start_index:end_index].lower() + raw_key[end_index:]
            print(f"{raw_key}")

    elif current[0] == 'Slice':
        start_index, end_index = int(current[1]), int(current[2])
        raw_key = raw_key[:start_index] + raw_key[end_index:]
        print(f"{raw_key}")



    command = input()
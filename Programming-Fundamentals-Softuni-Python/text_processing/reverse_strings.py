
while True:
    input_line = input()
    if input_line == 'end':
        break
    reversed_line = input_line[::-1]

    print(f'{input_line} = {reversed_line}')

first_string = input()
second_line = input()

for letters in second_line:
    second_line = second_line.replace(first_string, '')
print(second_line)
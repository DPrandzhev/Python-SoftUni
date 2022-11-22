input_line = input()
new_string = ""
for i in input_line:
    new_string += chr(ord(i) + 3)

print(new_string)
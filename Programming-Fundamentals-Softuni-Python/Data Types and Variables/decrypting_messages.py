key_integer = int(input())
number_of_lines = int(input())
output = ""
for i in range(number_of_lines):
    command = input()
    output += chr(key_integer + ord(command))

print(output)
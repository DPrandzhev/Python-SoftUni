string_one = input()
string_two = input()
last_printed_string = string_one

for char_index in range(len(string_one)):
    left_part = string_two[0:char_index + 1]
    right_part = string_one[char_index + 1:]
    current_string = left_part + right_part
    if current_string == last_printed_string:
        continue
    print(current_string)
    last_printed_string = current_string
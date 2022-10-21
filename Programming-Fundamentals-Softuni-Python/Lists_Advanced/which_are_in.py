first_string_line = input().split(", ")
second_string_line = input().split(", ")

new_list = []

for first_word in first_string_line:
    for second_word in second_string_line:
        if first_word in second_word and not first_word in new_list:
            new_list.append(first_word)
print(new_list)

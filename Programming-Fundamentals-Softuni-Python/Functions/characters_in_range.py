def in_range(first, second):
    list_of_chars = []
    for current_char in range(ord(first) + 1, ord(second)):
        list_of_chars.append(chr(current_char))
    return list_of_chars


first_char = input()
second_char = input()
result = in_range(first_char, second_char)
print(' '.join(result))

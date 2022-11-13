line_input = input().split()
final_string = ''

for word in line_input:
    final_string += word * len(word)

print(final_string)

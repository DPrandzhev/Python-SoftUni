input_string = input()
final_text = ""
last_letter = ""

for chr in input_string:
    if chr != last_letter:
        final_text += chr

    last_letter = chr

print(final_text)
some_text = input()
new_text = ""
strenght = 0

for index in range(len(some_text)):
    if strenght > 0 and some_text[index] != ">":
        strenght -= 1
    elif some_text[index] == ">":
        new_text += some_text[index]
        strenght += int(some_text[index + 1])
    else:
        new_text += some_text[index]

print(new_text)

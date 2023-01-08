import re
pattern = ''
line = input()

while line:
    matches = re.findall(pattern, line)
    if matches:
        print(' '.join(matches), end=' ')

    input_line = input()
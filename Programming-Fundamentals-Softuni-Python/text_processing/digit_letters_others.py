line_of_input = input()
digits = ''
lterres = ''
other = ''
for chr in line_of_input:
    if chr.isdigit():
        digits += chr
    elif chr.isalpha():
        lterres += chr
    else:
        other += chr

print(digits)
print(lterres)
print(other)

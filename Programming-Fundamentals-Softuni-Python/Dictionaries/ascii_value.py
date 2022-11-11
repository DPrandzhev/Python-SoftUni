input_line = input().split(", ")
ascii_dict = {}

for chr in input_line:
    if chr not in ascii_dict:
        ascii_dict[chr] = ord(chr)

print(ascii_dict)

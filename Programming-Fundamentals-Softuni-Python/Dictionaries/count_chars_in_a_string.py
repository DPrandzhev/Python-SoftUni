input_line = input().split(" ")
symbols = "".join(input_line)
dictionary = {}

for char in symbols:
    if char not in dictionary.keys():
        dictionary[char] = 0
    dictionary[char] += 1

for key, value in dictionary.items():
    print(f"{key} -> {value}")


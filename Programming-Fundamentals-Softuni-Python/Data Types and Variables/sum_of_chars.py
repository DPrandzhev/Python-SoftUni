number_of_inputs = int(input())
sum_of_chars = 0

for i in range(1, number_of_inputs + 1):
    char = input()
    char_num = ord(char)
    sum_of_chars += char_num

print(f"The sum equals: {sum_of_chars}")

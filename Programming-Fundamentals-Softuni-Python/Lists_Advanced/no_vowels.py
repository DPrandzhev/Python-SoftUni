input_text = input()
vowels = ['a', 'o', 'u', 'e', 'i']

# for i in input_text:
#     if i.lower() not in vowels:
#         print(i, end="")


result = [ch for ch in input_text if ch.lower() not in vowels]
print = (result)
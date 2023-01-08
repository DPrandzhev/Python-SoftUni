import re

input_line = input()
cool_treshold = 1

digits = r'\d'
emojis = r'(::|\*\*)([A-z][a-z]{2,}\s?)\1'

digits_match = re.findall(digits, input_line)
animals_match = re.findall(emojis, input_line)

for index in range(len(digits_match)):
    cool_treshold *= int(digits_match[index])


print(f'Cool threshold: {cool_treshold}')

print(f'{len(animals_match)}, emojis found in the text. The cool ones are:')

for animal in animals_match:
    acii_values = [ord(char) for char in animal[1]]
    sum_values = sum(acii_values)
    current_animal = animal[1]
    if sum_values >= cool_treshold:
        print(animal[0]+animal[1]+animal[0])



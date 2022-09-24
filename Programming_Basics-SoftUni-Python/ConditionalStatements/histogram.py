number_entries = int(input())

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0


for numbers in range(1, number_entries + 1):
    number_input = int(input())
    if number_input < 200:
        p1 = p1 + 1
    elif number_input <= 399:
        p2 = p2 + 1
    elif number_input <= 599:
        p3 = p3 + 1
    elif number_input <= 799:
        p4 = p4 + 1
    elif number_input >= 800:
        p5 = p5 + 1

percent_p1 = p1 / number_entries * 100
percent_p2 = p2 / number_entries * 100
percent_p3 = p3 / number_entries * 100
percent_p4 = p4 / number_entries * 100
percent_p5 = p5 / number_entries * 100



print(f"{percent_p1:.2f}%")
print(f"{percent_p2:.2f}%")
print(f"{percent_p3:.2f}%")
print(f"{percent_p4:.2f}%")
print(f"{percent_p5:.2f}%")
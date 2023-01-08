import re
participants = input().split(',')
false = True
some_info = input()
winners = []
distance = []
while false:

    if some_info == "end of race":
        break

    pattern_name = r'([A-Za-z]+)'
    pattern_digits = r'(\d)+'

    match_name = re.finditer(pattern_name, some_info)
    match_distance = re.findall(pattern_digits, some_info)
    if match_name in participants:
        winners.append(match_name)
        distance.append(match_distance)
    if len(winners) == 3:
        break
    some_info = input()

print(winners)
print(distance)

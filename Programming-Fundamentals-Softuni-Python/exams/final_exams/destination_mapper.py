import re
destinations = []
total_sum = 0
string = input()

pattern = r'(=|\/)([A-Za-z]{2,})\1'

places = re.findall(pattern, string)

for current_place in places:
    total_sum += len(current_place[1])
    destinations.append(current_place[1])


print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {total_sum}")
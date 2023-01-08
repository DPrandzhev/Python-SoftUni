import re
date = input()

pattern = r'(\d{2})([\/.-])([A-Z][a-z]{2})\2(\d{4})'

match = re.findall(pattern, date)


for result in match:
    print(f"Day: {result[0]}, Month: {result[2]}, Year: {result[3]}")
import re

line = input()
valid_url = []
pattern = r'(w{3})\.([A-z0-9]+)(\-[A-z0-9]+)*(\.[a-z]+)+'

while line:
    matches = re.search(pattern, line)

    if matches:
        valid_url.append(matches.group(0))

    line = input()

for url in valid_url:
    print(url)

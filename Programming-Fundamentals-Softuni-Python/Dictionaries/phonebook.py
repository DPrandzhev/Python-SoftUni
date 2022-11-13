phonebook = {}

while True:
    entry = input()
    if "-" not in entry:
        break

    name, number = entry.split("-")
    phonebook[name] = number

for check in range(int(entry)):
    searched_name = input()
    if searched_name not in phonebook.keys():
        print(f"Contact {searched_name} does not exist.")
    else:
        print(f"{searched_name} -> {phonebook[searched_name]}")
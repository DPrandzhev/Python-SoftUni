list_of_phones = input().split(", ")
command = input()

while command != "End":
    current_command = command
    action, item = current_command.split(" - ")

    if action == "Add":
        if item in list_of_phones:
            pass
        else:
            list_of_phones.append(item)

    elif action == "Remove":
        if item in list_of_phones:
            list_of_phones.remove(item)

    elif action == "Bonus phone":
        old_item, new_item = item.split(":")
        if old_item in list_of_phones:
            old_item_index = list_of_phones.index(old_item)
            list_of_phones.insert(old_item_index + 1, new_item)
        else:
            pass
    elif action == "Last":
        if item in list_of_phones:
            list_of_phones.remove(item)
            list_of_phones.append(item)

    command = input()

print(", ".join(list_of_phones))

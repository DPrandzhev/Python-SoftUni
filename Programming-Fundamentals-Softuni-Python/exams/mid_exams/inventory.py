journal = input().split(", ")
command = input()
inventory = journal
while command != "Craft!":

    action, item = command.split(" - ")
    if action == "Collect":
        if item in inventory:
            pass
        else:
            inventory.append(item)

    elif action == "Drop":
        if item in inventory:
            inventory.remove(item)

    elif action == "Combine Items":
        old_item, new_item = item.split(":")
        if old_item in inventory:
            old_item_index = inventory.index(old_item)
            inventory.insert(old_item_index + 1, new_item)
        else:
            pass

    elif action == "Renew":
        if item in inventory:
            inventory.remove(item)
            inventory.append(item)

    command = input()

print(", ".join(inventory))
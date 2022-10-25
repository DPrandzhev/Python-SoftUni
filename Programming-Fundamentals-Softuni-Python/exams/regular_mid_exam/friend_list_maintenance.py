def is_valid(index):
    if 0 <= index < len(lst_usernames):
        return True

lst_usernames = input().split(", ")
current_command = input()

while current_command != "Report":

    if "Change" in current_command:
        _, index, name = [int(x) if x.isdigit() else x for x in current_command.split()]
        if is_valid(index):
            print(f"{lst_usernames[index]} changed his username to {name}.")
            lst_usernames[index] = name
        # else:
        #     continue
    else:
        current_index = current_command.split()[-1]
        if "Blacklist" in current_command:
            if current_index in lst_usernames:
                name_index = lst_usernames.index(current_index)
                lst_usernames[name_index] = "Blacklisted"
                print(f"{current_index} was blacklisted.")
            else:
                print(f"{current_index} was not found.")

        elif "Error" in current_command:
            if is_valid(int(current_index)) and ("Lost" != lst_usernames[int(current_index)] != "Blacklisted"):
                print(f"{lst_usernames[int(current_index)]} was lost due to an error.")
                lst_usernames[int(current_index)] = "Lost"
            # else:
            #     continue


    current_command = input()

print(f"Blacklisted names: {len([x for x in lst_usernames if x == 'Blacklisted'])}")
print(f"Lost names: {len([x for x in lst_usernames if x == 'Lost'])}")
print(" ".join(lst_usernames))

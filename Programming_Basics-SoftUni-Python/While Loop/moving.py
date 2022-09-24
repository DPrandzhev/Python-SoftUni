space_w = int(input())
space_l = int(input())
space_h = int(input())

space_cubic = space_w * space_l * space_h
is_full = False


command = input()

while command != "Done":
    command_new = int(command)

    space_cubic -= command_new

    if space_cubic <= 0:
        is_full = True
        break

    command = input()
if is_full:
    print(f"No more free space! You need {abs(space_cubic)} Cubic meters more.")

else:
    print(f"{space_cubic} Cubic meters left.")
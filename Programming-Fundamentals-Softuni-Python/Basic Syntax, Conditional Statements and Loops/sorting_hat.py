student_name = input()
house = ""
is_vold = False
while student_name != "Welcome!":
    name_lenght = len(student_name)
    if student_name == "Voldemort":
        print("You must not speak of that name!")
        is_vold = True
        break

    if name_lenght < 5:
        house = "Gryffindor"
    elif name_lenght == 5:
        house = "Slytherin"
    elif name_lenght == 6:
        house = "Ravenclaw"
    elif name_lenght > 6:
        house = "Hufflepuff"

    print(f"{student_name} goes to {house}.")
    student_name = input()


if is_vold:
    pass
else:
    print("Welcome to Hogwarts.")

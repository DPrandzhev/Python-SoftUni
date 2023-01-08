prefered_meals = {}
disliked_meals = 0

def disliked_meal(guest_of_the_party, meal_to_serve):
    global disliked_meals
    if guest_of_the_party not in prefered_meals:
        print(f"{guest_of_the_party} is not at the party.")
    elif meal_to_serve not in prefered_meals[guest_of_the_party]:
        print(f"{guest_of_the_party} doesn't have the {meal_to_serve} in his/her collection.")
    elif meal_to_serve in prefered_meals[guest_of_the_party]:
        prefered_meals[guest_of_the_party].remove(meal_to_serve)
        disliked_meals += 1
        print(f"{guest_of_the_party} doesn't like the {meal_to_serve}.")


def liked_meal(guest_of_the_party, meal_to_serve):
    prefered_meals[guest_of_the_party] = prefered_meals.get(guest_of_the_party, [])
    if meal_to_serve not in prefered_meals[guest_of_the_party]:
        prefered_meals[guest_of_the_party].append(meal_to_serve)


command_func = {"Like": liked_meal, "Dislike": disliked_meal}

command = input()

while command != "Stop":
    current_command, guest_of_the_party, meal_to_serve = command.split("-")
    command_func[current_command](guest_of_the_party, meal_to_serve)
    command = input()

if prefered_meals:
    for guest in prefered_meals:
        print(f"{guest}: {', '.join(prefered_meals[guest])}")
print(f"Unliked meals: {disliked_meals}")


dungeon_rooms = [data.split() for data in input().split("|")]
room_counter = 0
health = 100
bitcoins = 0
is_dead = False
for i in dungeon_rooms:
    item, value = [int(x) if x.isdigit() else x for x in i]
    room_counter += 1

    if item == "potion":
        if health + value > 100:
            value = 100 - health
        health += value
        print(f"You healed for {value} hp.")
        print(f"Current health: {health} hp.")

    elif item == "chest":
        bitcoins += value
        print(f"You found {value} bitcoins.")

    else:
        health -= value
        if health > 0:
            print(f"You slayed {item}.")
        else:
            print(f"You died! Killed by {item}.")
            is_dead = True
            break

if is_dead:
    print(f"Best room: {room_counter}")
else:
    print(f"You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")

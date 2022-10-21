number_of_rooms = int(input())
free_chairs = 0
enough_chairs = True

for room_floor in range(1, number_of_rooms + 1):
    chairs, visitors = input().split(' ')
    visitors = int(visitors)


    if int(len(chairs)) >= visitors:
        free_chairs += abs(visitors - len(chairs))
    else:
        result = abs(visitors - len(chairs))
        print((f"{result} more chairs needed in room {room_floor}"))
        enough_chairs = False


if enough_chairs:
    print(f"Game On, {free_chairs} free chairs left")


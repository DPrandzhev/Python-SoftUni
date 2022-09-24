command = input()
num_coffees = 0
list_l = ["coding", "dog", "cat", "movie"]
list_c = ["CODING", "DOG", "CAT", "MOVIE"]

while command != "END":

    if command in list_l:
        num_coffees += 1
    elif command in list_c:
        num_coffees += 2
    else:
        pass

    command = input()


if num_coffees <= 5:
    print(num_coffees)
else:
    print("You need extra sleep")
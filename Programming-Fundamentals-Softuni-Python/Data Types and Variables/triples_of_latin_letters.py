num_index = int(input())

for a in range(0, num_index):
    for b in range(0, num_index):
        for c in range(0, num_index):
            print(f"{chr(97 + a)}{chr(97 + b)}{chr(97+c)}")
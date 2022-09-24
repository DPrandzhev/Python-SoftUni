max_num_first = int(input())
max_num_second = int(input())
max_num_third = int(input())

for pin1 in range(2, max_num_first + 1, 2):
    for pin2 in range(2, max_num_second + 1):
        for pin3 in range(2, max_num_third + 1, 2):
            if pin2 % pin2 == 0 and pin2 != 4 and pin2 <= 7:
                print(f" {pin1} {pin2} {pin3}")


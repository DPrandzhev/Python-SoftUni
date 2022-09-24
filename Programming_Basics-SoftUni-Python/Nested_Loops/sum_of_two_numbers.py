start = int(input())
final = int(input())
magic_number = int(input())
counter = 0
is_found = False

for i in range(start, final + 1):
    for y in range(start, final + 1):
        counter += 1
        if i + y == magic_number:
            is_found = True
            break
    if is_found:
        break
if is_found:
    print(f"Combination N:{counter} ({i} + {y} = {magic_number})")
else:
    print(f"{counter} combinations - neither equals {magic_number}")


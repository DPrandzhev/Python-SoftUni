output = {}
while True:
    resource = input()
    if resource == 'stop':
        break

    quantity = int(input())

    if resource not in output:
        output[resource] = 0
    output[resource] += quantity

for key, value in output.items():
    print(f" {key} -> {value}")

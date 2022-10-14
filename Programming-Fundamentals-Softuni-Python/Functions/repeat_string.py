starting_string = input()
counter = int(input())

# lambda solution
# repeat_string = lambda a, b: a * b
# result = repeat_string(starting_string, counter)
# print(result)


def rep_string(a, b):
    return a * b

print(rep_string(starting_string, counter))
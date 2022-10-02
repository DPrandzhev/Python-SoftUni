# head_input = input()
# body_input = input()
# tail_input = input()
#
# zoo_list = [head_input, body_input, tail_input]
# zoo_list[0], zoo_list[2] = zoo_list[2], zoo_list[0]
#
# print(zoo_list)

zoo_list = []

for i in range(3):
    data = input()
    zoo_list.append(data)

zoo_list[0], zoo_list[2] = zoo_list[2], zoo_list[0]
print(zoo_list)
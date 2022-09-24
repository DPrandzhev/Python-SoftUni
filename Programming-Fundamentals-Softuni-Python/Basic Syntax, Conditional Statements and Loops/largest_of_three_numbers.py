# num_one = int(input())
# num_two = int(input())
# num_tree = int(input())
#
# if num_one > num_two and num_one > num_tree:
#     print(num_one)
# elif num_two > num_one and num_two > num_tree:
#     print(num_two)
# else:
#     print(num_tree)
#

num_one, num_two, num_tree = int(input()), int(input()), int(input())
print(max(num_one, num_two, num_tree))

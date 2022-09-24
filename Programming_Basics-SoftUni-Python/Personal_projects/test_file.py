# capacity = float(input())
# command = input()
# current_suitcase = 0
# total_suitcase = 0
# num_suitcases = 0
#
# while command != "End":
#     current_suitcase = float(command)
#     if num_suitcases % 3 == 0:
#         current_suitcase = current_suitcase * 1.10
#     total_suitcase += current_suitcase
#     if total_suitcase > capacity:
#         break
#
#     num_suitcases += 1
#     current_suitcase = 0
#
#     command = input()
#
# if command == "End":
#     print("Congratulations! All suitcases are loaded!")
# if total_suitcase > capacity:
#     print("No more space!")
# print(f"Statistic: {num_suitcases} suitcases loaded.")


num = 1

while num <= 10:
    print(num)
    num += 1
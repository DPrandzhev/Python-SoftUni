import sys

max_score = - sys.maxsize
current_name = ""
current_best = ""

player_name = input()
while player_name != "END":
    total_goals = int(input())
    current_name = player_name

    if total_goals > max_score:
        max_score = total_goals
        current_best = current_name

    if total_goals >= 10:
        break

    player_name = input()

print(f"{current_best} is the best player!")

if max_score >= 3:
    print(f"He has scored {max_score} goals and made a hat-trick !!!")

else:
    print(f"He has scored {max_score} goals.")
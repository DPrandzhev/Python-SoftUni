actor_name = input()
academy_points = float(input())
count_people = int(input())

points_sum = academy_points

for i in range(1, count_people + 1):
    jury_name = input()
    jury_points = float(input())

    total_points = (len(jury_name) * jury_points) / 2
    points_sum = points_sum + total_points

    if points_sum >= 1250.5:
        break

if points_sum < 1250.5:
    diff = 1250.5 - points_sum
    print(f'Sorry, {actor_name} you need {diff:.1f} more!')

else:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {points_sum:.1f}!")
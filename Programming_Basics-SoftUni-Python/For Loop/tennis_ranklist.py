import math
number_of_tournaments = int(input())
starting_points = int(input())

points_w = 2000
points_f = 1200
points_sf = 720
points_sum = starting_points
wins = 0

for num in range(1, number_of_tournaments + 1):
    tournament_stage = input()

    if tournament_stage == "W":
        points_sum = points_sum + points_w
    elif tournament_stage == "F":
        points_sum = points_sum + points_f
    elif tournament_stage == "SF":
        points_sum = points_sum + points_sf

    if tournament_stage == "W":
        wins = wins + 1



avg_points = math.floor((points_sum - starting_points) / number_of_tournaments)
avg_wins = wins / number_of_tournaments * 100

print(f"Final points: {points_sum}")
print(f"Average points: {avg_points}")
print(f"{avg_wins:.2f}%")
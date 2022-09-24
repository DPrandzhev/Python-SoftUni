total_days = int(input())
total_raised_money = 0
win_counter = 0
lose_counter = 0
total_wins = 0
total_lose = 0
total_money = 0
for tournament in range(1, total_days + 1):
    game_name = input()
    while game_name != "Finish":
        outcome_of_game = input()
        if outcome_of_game == "win":
            total_raised_money += 20
            win_counter += 1
        elif outcome_of_game == "lose":
            lose_counter += 1
        game_name = input()

    if win_counter > lose_counter:
        total_raised_money *= 1.1

    total_wins += win_counter
    total_lose += lose_counter
    total_money += total_raised_money
    win_counter = 0
    lose_counter = 0
    total_raised_money = 0


if total_wins > total_lose:
    total_money *= 1.2
    print(f"You won the tournament! Total raised money: {total_money:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_money:.2f}")

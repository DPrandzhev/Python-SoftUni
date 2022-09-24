destination = input()


while destination != "End":
    needed_money = float(input())
    current_budget = 0
    while current_budget < needed_money:
        current_money = float(input())
        current_budget += current_money

    print(f"Going to {destination}!")
    destination = input()

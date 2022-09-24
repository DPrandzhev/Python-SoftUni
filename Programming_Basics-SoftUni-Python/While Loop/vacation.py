required_money = float(input())
available_money = float(input())

days = 0
days_spending = 0
is_broke = False

while available_money < required_money:
    if days_spending == 5:
        is_broke = True
        break

    action = input()
    budget = float(input())

    days += 1

    if action == "save":
        available_money += budget
        days_spending = 0

    elif action == "spend":
        available_money -= budget
        days_spending += 1
        if available_money <= 0:
            available_money = 0

if is_broke:
    print("You can't save the money.")
    print(f"{days}")

else:
    print(f"You saved the money for {days} days.")


budget = int(input())
command = input()
total_spent = 0
while command != "End":
    price = int(command)
    total_spent += price
    if total_spent > budget:
        print("You went in overdraft!")
        break

    command = input()

else:
    print("You bought everything needed.")
number_of_tabs = int(input())
base_salary = float(input())


salary = base_salary
for i in range(1, number_of_tabs + 1):
    tab = input()
    if tab == "Facebook":
        salary = salary - 150
    elif tab == "Instagram":
        salary = salary - 100
    elif tab == "Reddit":
        salary = salary - 50

    if salary <= 0:
        break

if salary <= 0:
    print("You have lost your salary.")
else:
    print(salary)

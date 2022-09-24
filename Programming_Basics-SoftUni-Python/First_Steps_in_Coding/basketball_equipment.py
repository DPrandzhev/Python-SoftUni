year_basketball_tax = int(input())

basketball_shoes = year_basketball_tax - (year_basketball_tax * 0.4)
basketball_clothes = basketball_shoes - (basketball_shoes * 0.2)
basketball_ball = basketball_clothes * 0.25
basketball_accessories = basketball_ball * 0.2

total_sum = basketball_accessories + basketball_shoes + basketball_ball + basketball_clothes + year_basketball_tax
print(total_sum)
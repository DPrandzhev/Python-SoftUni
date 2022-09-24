
# · Предпазен найлон - 1.50 лв. за кв. метър
#
# · Боя - 14.50 лв. за литър
#
# · Разредител за боя - 5.00 лв. за литър

nylon = int(input())
paint = int(input())
paint_sol = int(input())
work_hours = int(input())

nylon_sum = (nylon + 2) * 1.50
paint_sum = (paint * 1.1) * 14.50
paint_sol_sum = paint_sol * 5
bags = 0.4

total_sum = nylon_sum + paint_sum + paint_sol_sum + bags
workers_sum = (total_sum * 0.3) * work_hours

print(total_sum + workers_sum)

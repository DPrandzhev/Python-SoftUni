lenght_w = float(input())
widith_h = float(input())
lenght_cm = lenght_w * 100
widith_cm = widith_h * 100
workspace_widith = widith_cm - 100
desks_w = workspace_widith // 70
desks_h = lenght_cm // 120
total_desks = (desks_w * desks_h - 3)
print(total_desks)

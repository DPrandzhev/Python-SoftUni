lenght_cm = int(input())
widith_cm = int(input())
height_cm = int(input())
percent_sand = float(input())

volume = lenght_cm * widith_cm * height_cm
volume_in_lt = volume * 0.001
occupied_volume = percent_sand / 100
required_lt = volume_in_lt * (1-occupied_volume)
print(required_lt)
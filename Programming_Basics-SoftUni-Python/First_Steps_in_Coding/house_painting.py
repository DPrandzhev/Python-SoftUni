x = float(input())
y = float(input())
h = float(input())
side_wall = x * y
window = 1.5 * 1.5
two_walls = (2 * side_wall) - (2 * window)
back_wall = x * x
door = 1.2 * 2
front_back = (2 * back_wall) - door
total_area_green = (two_walls + front_back) / 3.4
print(f'{total_area_green:.2f}')
roof_sides = 2 * (x * y)
roof_triang = 2 * ((x * h) / 2)
total_area_red = (roof_sides + roof_triang) / 4.3
print(f'{total_area_red:.2f}')

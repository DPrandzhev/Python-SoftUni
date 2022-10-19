from math import floor as fl

def cartesian_system(a, b):
    if a <= b:
        return f"({x_one}, {x_two})"
    elif b <= a:
        return f"({y_one}, {y_two})"

x_one = fl(float(input()))
x_two = fl(float(input()))
y_one = fl(float(input()))
y_two = fl(float(input()))

sum_x = abs(x_one) + abs(x_two)
sum_y = abs(y_one) + abs(y_two)

print(cartesian_system(sum_x, sum_y))


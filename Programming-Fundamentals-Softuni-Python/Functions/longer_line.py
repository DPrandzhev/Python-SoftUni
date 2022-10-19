from math import floor as fl


def whats_closer(a, b, c, d):
    first = a + b
    second = c + d
    if first > second:
        if abs(x1) + abs(x2) > abs(y1) + abs(y2):
            return f"({y1}, {y2})({x1}, {x2})"
        else:
            return f"({x1}, {x2})({y1}, {y2})"

    elif first < second:
        if abs(z1) + abs(z2) > abs(v1) + abs(v2):
            return f"({v1}, {v2})({z1}, {z2})"
        else:
            return f"({z1}, {z2})({v1}, {v2})"

    else:
        if abs(z1) + abs(z2) > abs(v1) + abs(v2):
            return f"({v1}, {v2})({z1}, {z2})"
        else:
            return f"({z1}, {z2})({v1}, {v2})"


x1, x2, y1, y2 = fl(float(input())), fl(float(input())), fl(float(input())), fl(float(input()))
z1, z2, v1, v2 = fl(float(input())), fl(float(input())), fl(float(input())), fl(float(input()))

sum_x = (abs(x1) + abs(x2))
sum_y = (abs(y1) + abs(y2))
sum_z = (abs(z1) + abs(z2))
sum_v = (abs(v1) + abs(v2))

print(whats_closer(sum_x, sum_y, sum_z, sum_v))

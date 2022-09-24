import math

figure = input()

if figure == "square":
    size_square = float(input())
    area_square = size_square * size_square
    print(f'{area_square:.3f}')
elif figure == "rectangle":
    size_rec_a = float(input())
    size_rec_b = float(input())
    area_rec = size_rec_a * size_rec_b
    print(f'{area_rec:.3f}')
elif figure == "circle":
    r = float(input())
    area_circle = math.pi * (r ** 2)
    print(f'{area_circle:.3f}')
elif figure == "triangle":
    size_a = float(input())
    size_h = float(input())
    size_tri = (size_a * size_h) / 2
    print(f'{size_tri:.3f}')

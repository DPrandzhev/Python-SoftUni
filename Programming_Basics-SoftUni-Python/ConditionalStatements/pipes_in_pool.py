volume_pool = int(input())
pipe_one = int(input())
pipe_two = int(input())
hours_h = float(input())

pipe_volume_one = pipe_one * hours_h
pipe_volume_two = pipe_two * hours_h

volume_water = pipe_volume_one + pipe_volume_two

percentage_water = (volume_water / volume_pool) * 100
pipe_one_percent = (pipe_volume_one / volume_water) * 100
pipe_two_percent = (pipe_volume_two / volume_water) * 100

extra_water = abs(volume_pool - volume_water)

if volume_water <= volume_pool:
    print(f"The pool is {percentage_water}% full. Pipe 1: {pipe_one_percent:.2f}%. Pipe 2: {pipe_two_percent:.2f}%")

else:
    print(f"For {hours_h} hours the pool overflows with {extra_water:.2f} liters.")

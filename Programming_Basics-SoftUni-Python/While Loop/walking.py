
command = input()
daily_steps = 0
# is_reached = False

while command != "Going home":

    daily_steps += int(command)

    if daily_steps >= 10000:
        # is_reached = True
        break

    command = input()

if command == "Going home":
    command = input()
    daily_steps += int(command)

diff = abs(daily_steps - 10000)

if daily_steps >= 10000:
    print(f"Goal reached! Good job!")
    print(f"{diff} steps over the goal!")

else:
    print(f"{diff} more steps to reach goal.")
temperature = float(input())
if temperature <= 11.9:
    print("Cold")
elif temperature <= 14.9:
    print("Cool")
elif temperature <= 20.0:
    print("Mild")
elif temperature <= 25.9:
    print("Warm")
elif temperature <= 35:
    print("Hot")
else:
    print("unknown")


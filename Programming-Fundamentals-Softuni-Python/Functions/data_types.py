def data_type(x, y):
    if x == "int":
        return f"{int(y) * 2}"
    elif x == "real":
        return f" {float(y) * 1.5:.2f}"
    elif x == "string":
        return f"${y}$"


first_line = input()
second_line = input()

print(data_type(first_line, second_line))

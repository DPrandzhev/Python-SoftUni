text = input()
while text != "End":
    if text != "SoftUni":
        for i in text:
            print(i * 2, end="")
        print()
    else:
        pass
    text = input()


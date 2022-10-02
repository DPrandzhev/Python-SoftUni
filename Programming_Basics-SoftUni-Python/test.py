n1 = int(input())
n2 = int(input())
operator = input()
result = 0
even_odd = 0
divide_error = False

if operator == "+":
    result = n1 + n2

elif operator == "-":
    result = n1 - n2

elif operator == "*":
    result = n1 * n2

elif operator == "/":
    if n2 == 0:
        divide_error = True
    else:
       result = n1 / n2

elif operator == "%":
    if n2 == 0:
        divide_error = True
    else:
        result = n1 % n2

if operator == "+" or operator == "-" or operator == "*":
    if result % 2 == 0:
        even_odd = "even"
    else:
        even_odd = "odd"
    print(f"{n1} {operator} {n2} = {result} - {even_odd}")

elif divide_error:
    print(f"Cannot divide {n1} by zero")

elif operator == "/":
    print(f"{n1} {operator} {n2} = {result:.2f}")

elif operator == "%":
    print(f"{n1} {operator} {n2} = {result}")


    43 :.2f
    21 result == n1 / n2
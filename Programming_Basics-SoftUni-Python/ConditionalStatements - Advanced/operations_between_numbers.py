`number_one = int(input())
number_two = int(input())
operator = input()
result = 0
even_odd = 0
divide_error = False

if operator == "+":
    result = number_one + number_two

elif operator == "-":
    result = number_one - number_two

elif operator == "*":
    result = number_one * number_two

elif operator == "/":
    if number_two == 0:
        divide_error = True
    else:
        result = number_one / number_two

elif operator == "%":
    if number_two == 0:
        divide_error = True
    else:
        result = number_one % number_two



if operator == "+" or operator == "-" or operator == "*":
    if result % 2 == 0:
        even_odd = "even"
    else:
        even_odd = "odd"
    print(f"{number_one} {operator} {number_two} = {result} - {even_odd}")
elif divide_error:
    print(f"Cannot divide {number_one} by zero")

elif operator == "/":
    print(f"{number_one} {operator} {number_two} = {result:.2f}")

elif operator == "%":
    print(f"{number_one} {operator} {number_two} = {result}")`
x = int(input())
y = int(input())

print("Before:")
print(f"a = {x}")
print(f"b = {y}")

temp = x
x = y
y = temp

print("After:")
print(f"a = {x}")
print(f"b = {y}")
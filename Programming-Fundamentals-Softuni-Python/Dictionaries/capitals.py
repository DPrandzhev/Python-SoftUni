countries = input().split(', ')
capitals = input().split(', ')

result = {countries[index]: capitals[index] for index in range(len(countries))}

for key, value in result.items():
    print(f"{key} -> {value}")

    
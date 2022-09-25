centuries = int(input())

in_years = centuries * 100
in_days = int(in_years * 365.2422)
in_hours = in_days * 24
in_minutes = in_hours * 60

print(f"{centuries} centuries = {in_years} years = {in_days} days = {in_hours} hours = {in_minutes} minutes")
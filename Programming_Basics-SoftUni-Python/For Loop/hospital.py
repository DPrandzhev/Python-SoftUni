time_period = int(input())
doctors = 7
days = 0

treated_patients = 0
untreated_patients = 0

for i in range(1, time_period+1):
    patients = int(input())
    days += 1

    if days % 3 == 0:
        if untreated_patients > doctors:
            doctors += 1

    if patients <= doctors:
        treated_patients += patients

    elif patients > doctors:
        untreated_patients += abs(patients - doctors)
        treated_patients = doctors + treated_patients

print(f"Treated patients: {treated_patients}.")
print(f"Untreated patients: {untreated_patients}.")
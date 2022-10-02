number_of_entries = int(input())
list_positives = []
list_negatives = []

for lst in range(number_of_entries):
    data = int(input())

    if data >= 0:
        list_positives.append(data)
    else:
        list_negatives.append(data)

print(list_positives)
print(list_negatives)
print(f"Count of positives: {len(list_positives)}")
print(f"Sum of negatives: {sum(list_negatives)}")

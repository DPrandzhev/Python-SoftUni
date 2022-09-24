pages_in_book = int(input())
pages_per_hour = int(input())
days_due = int (input())

total_reading_time = int(pages_in_book / pages_per_hour)
required_reading_time = int(total_reading_time / days_due)

print(required_reading_time)

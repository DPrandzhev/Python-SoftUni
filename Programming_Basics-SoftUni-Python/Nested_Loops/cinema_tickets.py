movie_title = input()

counter_standard = 0
counter_kid = 0
counter_student = 0

while movie_title != "Finish":
    available_seats = int(input())
    sold_seats = 0
    for tickets in range(available_seats):
        current_ticket = input()
        if current_ticket == "End":
            break
        elif current_ticket == "student":
            counter_student += 1
        elif current_ticket == "standard":
            counter_standard += 1
        elif current_ticket == "kid":
            counter_kid += 1

        sold_seats += 1
    percent_full_hall = sold_seats / available_seats * 100
    print(f"{movie_title} - {percent_full_hall:.2f}% full.")


    movie_title = input()

total_tickets = counter_student + counter_standard + counter_kid
print(f"Total tickets: {total_tickets}")
percent_student_tk = counter_student / total_tickets * 100
print(f"{percent_student_tk:.2f}% student tickets.")
percent_standard_tk = counter_standard / total_tickets * 100
print(f"{percent_standard_tk:.2f}% standard tickets.")
percent_kid_tk = counter_kid / total_tickets * 100
print(f"{percent_kid_tk:.2f}% kids tickets.")
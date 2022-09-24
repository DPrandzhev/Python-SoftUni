hours = int(input())
day = input()

# working hours - 10 - 18
# working days - Monday - Sat

if 10 <= hours <= 18:
    if day == "Monday" \
    or day == 'Tuesday' \
    or day == 'Wednesday' \
    or day == 'Thursday' \
    or day == 'Friday' \
    or day ==  'Saturday':
        print('open')
    else:
        print('closed')
else:
    print('closed')
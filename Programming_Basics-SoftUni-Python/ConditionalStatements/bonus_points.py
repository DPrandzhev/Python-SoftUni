points = int((input()))
bonus = 0

if points <= 100:
    bonus = 5
elif points <= 1000:
    bonus = points * 0.2
elif points >= 1001:
    bonus = points * 0.1

if points % 2 == 0:
    bonus += 1
elif points % 10 == 5:
    bonus = bonus + 2

print (bonus)
print (bonus + points)

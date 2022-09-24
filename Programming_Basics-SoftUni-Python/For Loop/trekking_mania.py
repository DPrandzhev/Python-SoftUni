number_groups = int(input())

sum_mussala = 0
sum_monblan = 0
sum_kilimanjaro = 0
sum_k2 = 0
sum_everest = 0

total_ppl_count = 0


for i in range(1, number_groups + 1):
    people_in_group = int(input())
    total_ppl_count = total_ppl_count + people_in_group
    if people_in_group <= 5:
        sum_mussala = sum_mussala + people_in_group
    elif people_in_group <= 12:
        sum_monblan = sum_monblan + people_in_group
    elif people_in_group <= 25:
        sum_kilimanjaro = sum_kilimanjaro + people_in_group
    elif people_in_group <= 40:
        sum_k2 = sum_k2 + people_in_group
    else:
        sum_everest = sum_everest + people_in_group

p_mussala = sum_mussala / total_ppl_count * 100
p_monblan = sum_monblan / total_ppl_count * 100
p_kilimanjaro = sum_kilimanjaro / total_ppl_count * 100
p_k2 = sum_k2 / total_ppl_count * 100
p_everest = sum_everest / total_ppl_count * 100

print(f"{p_mussala:.2f}%")
print(f"{p_monblan:.2f}%")
print(f"{p_kilimanjaro:.2f}%")
print(f"{p_k2:.2f}%")
print(f"{p_everest:.2f}%")
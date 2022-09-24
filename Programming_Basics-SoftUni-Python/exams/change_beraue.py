bitcoin_input = int(input())
china_iuan_input = float(input())
commission = float(input())

bitcoin = 1168
china_iuan = 0.15 * 1.76
dollar = 1.76
euro = 1.95

total_sum = (bitcoin_input * bitcoin) + (china_iuan_input * china_iuan)
total_sum_eur = total_sum / euro

final_sum = total_sum_eur - ((commission / 100) * total_sum_eur)
print(f"{final_sum:.2f}")
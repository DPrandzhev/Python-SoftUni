tickets_sting = input().split(", ")
symbols = ['@', '#', '$', '^']


def get_max_in_a_row(string, symbol):
    next_, current = 0, 0
    for x in range(len(string)):
        if string[x] == symbol:
            next_ += 1
            if x == len(string) - 1:
                if current < next_:
                    current = next_
        else:
            if current < next_:
                current = next_
            next_ = 0
    return current


for ticket_characters in tickets_sting:
    ticket_characters = ticket_characters.replace(" ", "")
    if len(ticket_characters) == 20:
        how_long = int(len(ticket_characters) / 2)
        left_side, right_side = ticket_characters[:how_long], ticket_characters[how_long:]
        for symbol in symbols:
            sum_of_l, sum_of_r = get_max_in_a_row(left_side, symbol), get_max_in_a_row(right_side, symbol)
            if sum_of_l == sum_of_r == 10:
                print(f'ticket "{ticket_characters}" - 10{symbol} Jackpot!')
                break
            winners_price = min(sum_of_l, sum_of_r)
            if winners_price >= 6:
                print(f'ticket "{ticket_characters}" - {winners_price}{symbol}')
                break
        else:
            print(f'ticket "{ticket_characters}" - no match')
    else:
        print("invalid ticket")

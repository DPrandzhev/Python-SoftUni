def tribonnacci(x):
    tribonnacci_list = [1, 0, 0]
    for num in range(x):
        next = sum(tribonnacci_list)
        print(next, end=" ")
        tribonnacci_list.append(next)
        tribonnacci_list.pop(0)

amount_of_numbers = int(input())

tribonnacci(amount_of_numbers)
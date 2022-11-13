#print("Hello SoftUni")
# some_text = 'Hello SoftUni'
# print(some_text)
#


# def main():
#     message = "hd72ww$rt101wqar$r108wwa$108wwe$qwry111rw$dd32wwqwq$wnnf87qw$serty111we$jjfvb114wq$qqwtu108wq$req100wq$wq33"
#     message_list = message.split("$")
#     lst_prime = []
#     for word in message_list:
#         digit = ''.join([num for num in word if num.isdigit()])
#         lst_prime.append(chr(int(digit)))
#     res = [ch for ch in lst_prime]
#     print("".join(res))



# ---HelloSoftUni---

def main():
    message = "qqa@72$pk&101$ds^sd108$urd@@108$kkrs111$sof@ty32$scvb83$istber111$or(g102$kssr116w$cx/x85e$vx%110$dyu105"
    message_list = message.split("$")
    lst_prime = []
    for word in message_list:
        digit = ''.join([num for num in word if num.isdigit()])
        lst_prime.append(chr(int(digit)))
    res = [ch for ch in lst_prime]
    print("".join(res))


if __name__ == "__main__":
    main()


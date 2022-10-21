def swap(letters):
    if len(letters) != 1:
        start = letters[0]
        end = letters[-1]
        swap = end + letters[1:-1] + start
    else:
        swap = letters

    return swap


encrypted_message = input().split("$")
first_letter_lst = []
rest_of_the_word = []
decrypted_word = []

for word in encrypted_message:
    digit = ''.join([num for num in word if num.isdigit()])
    first_letter_lst.append(chr(int(digit)))
    letters = "".join([chr for chr in word if chr.isidentifier()])
    rest_of_the_word.append(letters)

for char in rest_of_the_word:
    result = swap(char)
    decrypted_word.append(result)


for n, w in zip(first_letter_lst, decrypted_word):
    print(f"{n}{w}", end=" ")

print(first_letter_lst)
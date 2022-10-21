def palindrome_check(word):
    if word == word[::-1]:
        return word

input_line = input().split(" ")
palindrome = input()

palindrome_lst = [word for word in input_line if palindrome_check(word)]

# for current_word in input_line:
#     palindrome_check(current_word)
#     palindrome_lst.append(current_word)
number_of_repeats = palindrome_lst.count(palindrome)

print(palindrome_lst)
print(f"Found palindrome {number_of_repeats} times")

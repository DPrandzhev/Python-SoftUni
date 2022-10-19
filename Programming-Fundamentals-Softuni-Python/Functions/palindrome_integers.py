def palindrome_checker(all_numbers):
    result = [True if number == number[::-1] else False for number in all_numbers]
    return result
    # result = []
    # for number in all_numbers:
    #     if number == number[::-1]:
    #         result.append(True)
    #     else:
    #         result.append(False)
    # return result


numbers = input().split(", ")
final_result = palindrome_checker(numbers)
for boolean in final_result:
    print(boolean)
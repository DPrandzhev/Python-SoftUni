def password_validation(password):
    list_with_errors = []
    if not 6 <= len(password) <= 10:
        list_with_errors.append("Password must be between 6 and 10 characters")
    counter_of_digits = 0
    for character in password:
        if not character.isdigit() and not character.isalpha():
            list_with_errors.append("Password must consist only of letters and digits")
            break
        elif character.isdigit():
            counter_of_digits += 1
    if counter_of_digits < 2:
        list_with_errors.append("Password must have at least 2 digits")
    return list_with_errors


current_password = input()
errors = password_validation(current_password)
if not errors:
    print("Password is valid")
else:
    for error in errors:
        print(error)
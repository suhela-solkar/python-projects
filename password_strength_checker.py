def check_password_strength(password):
    length = len(password)

    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        else:
            has_special = True

    score = sum([has_upper, has_lower, has_digit, has_special])

    if length >= 8 and score == 4:
        return "Strong Password"
    elif length >= 6 and score >= 2:
        return "Medium Password"
    else:
        return "Weak Password"


password = input("Enter your password: ")
result = check_password_strength(password)
print(result)

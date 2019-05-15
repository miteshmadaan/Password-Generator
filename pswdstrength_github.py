#checking password strength
def strength_calculator(password):
    #rejecting password if no of lower case letters are less than 1 or no of upper case letters are less than 2 or no of digits are less than 3
    if sum(c.islower() for c in password)<1 or sum(c.isupper() for c in password)<2 or sum(c.isdigit() for c in password)<3:
        return 0
    #1 length of password
    length = len(password)
    score = length * 4
    #2 no of upper case letters
    count = 0
    for c in password:
        if c.isupper():
            count += 1
    score += (length - count) * 2
    #3 no of lower case letters
    count = 0
    for c in password:
        if c.islower():
            count += 1
    score += (length - count) * 2
    #4 no of digits
    count = 0
    for c in password:
        if c.isdigit():
            count += 1
    score += count * 4
    #5 no of special characters
    count = 0
    for c in password:
        if not c.isalnum():
            count += 1
    score += count * 6
    #6 if password lacks any symbol/special character
    if password.isalpha():
        score -= length
    #7 if password contains only digits
    if password.isdecimal():
        score -= length
    # 8 checking for sequential letters
    digit = ''.join(i for i in password if i.isdigit())
    if '0123456789'.find(digit):
        score -= len(digit)*3
    # 8 checking for sequential numbers
    data = ''.join(i for i in password if i.isalpha())
    if 'abcdefghijklmnopqrstuvwxyz'.find(data):
        score -= len(data)*3
    #returning value of strength of password
    return score




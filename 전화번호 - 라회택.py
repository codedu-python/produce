def change_num(number):
    return '*'*len(number[:-4]) + number[-4:]

print(change_num('01012345678'))
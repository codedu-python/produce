phonenumber = input("핸드폰번호 11자리를 입력하세요.")

def masking(phonenumber):
    return phonenumber[0:7]+'*'*len(phonenumber[7:])

print(masking(phonenumber))

def printTriangle(num):
    s = ""
    i = 0
    while i < num:
        i = i +1
        s = s + "*"*i + "\n"

    #함수를 완성하세요

    return s


# 아래는 테스트로 출력해 보기 위한 코드입
print(printTriangle(3))

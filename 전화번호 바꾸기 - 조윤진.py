N = input("전화번호를 입력하세요(-자 제외) : ")

def PrivateN(N):
    i = len(N)
    print("{}".format(((i - 4)*'*')+ N[-4:]))
PrivateN(N)

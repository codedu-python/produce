def hashard(N):
    s = sum([int(i) for i in N])
    if int(N) % s == 0:
        return True
    else:
        return False

Num = input("숫자를 입력하세요")

print(hashard(Num))
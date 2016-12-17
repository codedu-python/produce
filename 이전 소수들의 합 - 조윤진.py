a = [2]
N = int(input("숫자를 입력하세요 : "))
def addPrime(N):
    s = 0
    t = 3
    if N <= 2:
        return 0
    elif N == 3:
        return 2
    else :
        while t < N:
            for numbers in range(2, t):
                if t % numbers == 0:
                    break
            else:
                a.append(t)
            t+=1
        for i in a:
            s = s + i
        return s

print ("결과는 {}입니다." .format(addPrime(N)))

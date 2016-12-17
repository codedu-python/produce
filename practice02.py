N = int(input("숫자를 입력하세요 : "))
def divideNumber(N):
    number = N
    for i in range (2, N+1):
        while i <= number:
            if number % i == 0:
                number = number/i
                print (i)
            else:
                break

divideNumber(N)

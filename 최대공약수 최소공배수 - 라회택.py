A = int(input('첫번째 숫자를 입력하세요'))
B = int(input('두번째 숫자를 입력하세요'))

def insu(num):
    insu = set()
    for i in range(1, num + 1):
        if num % i == 0:
            insu.add(i)
    return insu
insu_A = insu(A)
insu_B = insu(B)

inter_insu = insu_A & insu_B
max_insu = max(inter_insu)
if max_insu != 1:
    print('두 수의 최대공약수는 ',max_insu)
else:
    print('최대공약수 없음')

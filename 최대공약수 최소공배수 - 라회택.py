from collections import Counter

A = int(input('첫번째 숫자를 입력하세요'))
B = int(input('두번째 숫자를 입력하세요'))

#최대공약수입니다.
def insu(num):
    insu = {i for i in range(1, num+1) if num % i == 0}
    return insu

max_insu = max(insu(A) & insu(B))
if max_insu != 1:
    print('두 수의 최대공약수는 ',max_insu)
else:
    print('최대공약수 없음')

#최소공배수입니다.
def soinsubunhae(num):
    soinsu = []
    for i in range (2, num+1):
        while i <= num:
            if num % i == 0:
                num = num/i
                soinsu.append(i)
            else:
                break

    return soinsu

soinsu_A = Counter(soinsubunhae(A))
soinsu_B = Counter(soinsubunhae(B))
LCM = list((soinsu_A|soinsu_B).elements())
multi = 1
for number in LCM:
    multi *= number
print("두 수의 최소공배수는 ", multi)

from collections import Counter

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


def soinsubunhae(num):
    insu = []
    for i in range(1, num+1):
        if num % i == 0:
            insu.append(i)
    Num_prime = list(range(2, num))
    for n in Num_prime:
        for compare in range(n+1, num):
            if compare % n ==0 and compare in Num_prime:
                Num_prime.remove(compare)


    soinsu = []
    for primeinsu in insu:
        if primeinsu in Num_prime:
            count = 0
            while True:
                if num/primeinsu == int(num/primeinsu):
                    count += 1
                    num = int(num/primeinsu)
                    soinsu.append(primeinsu)
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
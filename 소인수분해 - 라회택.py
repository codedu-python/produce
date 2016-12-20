from collections import Counter

N = int(input("숫자를 입력하세요"))


def soinsubunhae(num):
    soinsu = []
    for i in range (2, num+1):
        while i <= num:
            if num % i == 0:
                num = num/i
                soinsu.append(i)
            else:
                break
    return dict( Counter(soinsu))

print(soinsubunhae(N))

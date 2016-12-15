N = int(input("숫자를 입력하세요"))
soinsu = []
for i in range(1, N+1):
    if N % i == 0:
        soinsu.append(i)

print(soinsu)
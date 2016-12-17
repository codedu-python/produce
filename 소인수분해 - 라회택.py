N = int(input("숫자를 입력하세요"))
insu = []
for i in range(1, N+1):
    if N % i == 0:
        insu.append(i)
Num_prime = list(range(2, N))
for n in Num_prime:
    for compare in range(n+1, N):
        if compare % n ==0 and compare in Num_prime:
            Num_prime.remove(compare)


soinsu = []
for num in insu:
    if num in Num_prime:
        print(num)
        count = 0
        while True:

            print(count)
            if N/num == int(N/num):
                count += 1
                N = int(N/num)
            else:
                break
        soinsu.append((num, count))
print(soinsu)
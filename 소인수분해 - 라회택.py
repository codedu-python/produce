N = int(input("숫자를 입력하세요"))


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
            print(primeinsu)
            count = 0
            while True:

                print(count)
                if num/primeinsu == int(num/primeinsu):
                    count += 1
                    num = int(num/primeinsu)
                else:
                    break
            soinsu.append((primeinsu, count))
    return soinsu

print(soinsubunhae(N))
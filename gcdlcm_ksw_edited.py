print("최대공약수와 최소공배수를 구하는 프로그램입니다.")
a = int(input('첫 번째 수를 입력하세요.'))
b = int(input('두 번째 수를 입력하세요.'))
def comprime(a, b)
    for i in range(2, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            return False
        return True
def gcd(a, b):
    if a < b:
        (a, b) = (b, a)
    while b != 0:
        if comprime(a, b) == True:
            a = max(i)
            b = a % b
        else:
            a = 1
    return a
gcd_value = gcd(a,b)
def lcm(a, b):
    if (gcd_value == 0): return 0
    return abs( (a * b) / gcd_value )
lcm_value = lcm(a,b)
print("최대공약수는 %d, 최소공배수는 %d입니다."%(gcd_value, lcm_value))

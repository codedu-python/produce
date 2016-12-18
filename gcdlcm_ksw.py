print("최대공약수와 최소공배수를 구하는 프로그램입니다.")
a = int(input('첫 번째 수를 입력하세요.'))
b = int(input('두 번째 수를 입력하세요.'))
def gcd(a, b):
    while (b!= 0):
        temp = a % b
        a = b
        b = temp
        return abs(a)#abs()가 절대값 함수라네요~

def lcm(a, b):
    gcd_value = gcd(a, b)
    if (gcd_value == 0): return 0
    return abs( (a * b) / gcd_value )

gcd_value = gcd(a,b)
lcm_value = lcm(a,b)
print("최대공약수는 %d, 최소공배수는 %d입니다."%(gcd_value, lcm_value))

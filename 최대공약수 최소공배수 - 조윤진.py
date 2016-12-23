A = int(input("첫 번째 수를 입력하세요 : "))
B = int(input("두 번째 수를 입력하세요 : "))

def gcd (a, b):
    if a < b:
        (a, b) = (b, a)
    while  b != 0:
        r = a % b
        a = b
        b = r
    return a

def gab (a, b):
    return a*b/gcd(a,b)

print ("두 수의 최대공약수는 {}입니다." .format(gcd(A, B)))
print ("두 수의 최소공배수는 {}입니다." .format(gab(A, B)))

def alpha_string46(s):
    alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u',
             'v','w','x','y','z']
    if len(s) == 4 or len(s) == 6:
        for i in alpha:
            if s.count(i)==0:
                r = True
            else:
                r = False
    else:
        r = False
    return r

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( alpha_string46("a234") )
print( alpha_string46("1234") )
print( alpha_string46("6q00"))

print("하샤드수인지 파악하기 위한 프로그램입니다.")
number = int(input("수를 입력하세요: "))
def sum_digit(number):
    if number < 10:
        return number;
    return (number % 10) + sum_digit(number // 10)#//가 나눗셈의 몫이라네요~
sum_number = sum_digit(number)
def harshad(number):
    if number % sum_number == 0:
        print("하샤드수입니다.")
    else:
        print("하샤드수가 아닙니다.")
harshad(number)

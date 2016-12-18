import datetime

print("2017년 A월 B일의 요일을 구하는 프로그램입니다.")

A = 1
B = 1
weekday = 0
days_of_week = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
def input_mon_day():
    global A, B, weekday
    try:
        A = int(input("월을 입력하세요  "))
        B = int(input("일을 입력하세요  "))
        weekday = datetime.date(2017, A, B).weekday()
    except ValueError:
        print('잘못된 값을 입력하셨습니다.\n 다시 입력하십시오.')
        input_mon_day()
        print("\n")
input_mon_day()
print(days_of_week[weekday])
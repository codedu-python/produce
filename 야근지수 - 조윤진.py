list_works = input("해야 할 일의 양을 숫자만 한 칸씩 띄어 입력하세요 : ").split()
left_time = int(input("퇴근까지 남은 시간을 입력하세요 : "))
works = list(map(int, list_works))
def noOvertime(left_time, works):
    while left_time > 0:
        works.sort()
        works.reverse()
        works[0] -= 1
        left_time -= 1
    return works

def todo_work(left):
    sum = 0
    for i in left:
        sum = sum + i**2
    return sum

noOvertime(left_time, works)
print ("퇴근까지 해야 할 일의 양은 {}입니다. ".format(todo_work(works)))

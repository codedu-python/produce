def Overtime(time, works):

    while time > 0:
        works.sort()
        works.append(works.pop(-1)-1)
        time = time - 1
    overtime = 0
    for work in works:
        overtime += work**2

    return overtime

print(Overtime(4, [4,3,3]))
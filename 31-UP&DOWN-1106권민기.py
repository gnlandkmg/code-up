import random
a = random.randint(1,20)
while True:
    pl= int(input())
    if pl == 0:
        break
    elif pl == a:
        print("정답!")
        break
    elif pl < a:
        print("업")
    elif pl > a:
        print("다운")
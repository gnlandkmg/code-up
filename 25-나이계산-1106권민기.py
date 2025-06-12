a,b = map(int,input().split(','))
if b == 3 or b ==4:
    c = a // 10000
    print(26-c)

elif b == 1 or b ==2:
    c = (a // 10000)
    print(c-62)
else:
    print("존재하지 않습니다.")
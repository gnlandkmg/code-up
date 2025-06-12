try:
    a,b,c = map(int,input("ax + b = c 중 a,b,c를 공백으로 구분해 넣어주세요.").split())
except ValueError:
    print("정수가 아닙니다.")
else:
    if a == 0:
        if c-b == 0:
            print("해가 무수히 많습니다.")
        elif c-b != 0:
            print("해가 존재하지 않습니다.")
    else:
        print("-"*30)
        print(f"{a}x + {b} = {c}")
        print(f"{a}x = {c} - {b}")
        print(f"{a}x = {c-b}")
        if a == 1:
            print("-"*30)
            print(f"{a}x + {b} = {c} 의 해는 x = {c-b} 입니다.")
        else:
            print(f"x = {c-b}/{a}")
            print(f"x = {(c-b)/a}")
            print("-"*30)
            print(f"{a}x + {b} = {c} 의 해는 x = {(c-b)/a} 입니다.")
            
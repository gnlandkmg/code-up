a = int(input())
if a == 1 or a== 2:
   x,y = map(int,input().split())
else:
    r= int(input())
if a == 1:
    print(f"삼각형의 넓이는 {x*y/2}cm^2입니다.")
elif a ==2:
    print(f"사각형의 넓이는 {x*y}cm^2입니다.")
elif a == 3:
    print(f"원의 넓이는 {r*r*3.14}cm^2입니다.")
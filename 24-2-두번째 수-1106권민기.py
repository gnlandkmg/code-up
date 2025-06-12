a,b,c = map(int,input().split())
if c<=a<=b or b<=a<=c:
    print(a)
if c<=b<=a or a<=b<=c:
    print(b)
if b<=c<=a or a<=c<=b:
    print(f"제일 작은 두번째 수는 {c}입니다.")
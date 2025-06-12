result = 0
num = 0
while True:
    try:
        n = int(input("점수: "))
    except ValueError:
        break
    else:
        result = result + n
        num = num +1
print(f"합계: {result}")
print(f"평균: {result/num}")
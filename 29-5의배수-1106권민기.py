while True:
    n = int(input())
    if n == 0:
        break
    elif n % 5 == 0:
        print("5의 배수입니다")
    else:
        print("5의 배수가 아닙니다.")
print("프로그램 종료")
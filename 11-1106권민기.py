a =["홍길동","일지매"]
print(f"현재 수강 신청자는 {a} 입니다.")
a.append(input("추가할 학생 이름:"))
print(f"{a[-1]} 학생의 신청이 완료되었습니다.")
print(f"현재 이 과목이 신청자는 {a} 입니다.")
while True:
    i = int(input("1(추가),2(철회),3(변경),0(종료)"))
    if i == 1:
        a.append(input("추가할 학생 이름:"))
        print(f"{a[-1]} 학생의 신청이 완료되었습니다.")
        print(f"현재 이 과목이 신청자는 {a} 입니다.")
    elif i == 2:
        a.append(input("철회할 학생 이름:"))
        print(f"{a[-1]} 학생의 철회가 완료되었습니다.")
        print(f"현재 이 과목이 신청자는 {a} 입니다.")
    
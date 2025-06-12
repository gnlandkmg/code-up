import random
player = int(input("가위(1),바위(2),보(3) 중에 선택:"))
com = random.randrange(1,4)
if player == com:
    print(f"player:{player},com:{com} 비김")
elif (player == 1 and com == 2) or (player == 2 and com == 3) or (player == 3 and com == 1):
    print(f"player:{player},com:{com} 졌음")
else:
    print(f"player:{player},com:{com} 이김")
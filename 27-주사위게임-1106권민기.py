import random
player1,player2 = map(int,input("2개 입력(1~6,중복허용):").split())
com1=random.choice(range(1,7))
com2=random.choice(range(1,7))


print(f"컴퓨터:{com1,com2}당신:{player1,player2}")
if (com1 == player1 and com2 == player2) or (com1 == player2 and com2 == player1):
    print("1등")
elif (com1 == player1 or com2 == player2) or (com1 == player2 or com2 == player1):
    print("2등")
else:
    print("꽝!")

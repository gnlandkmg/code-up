a = int(input())
tru = 0
if a !=1:
    for i in range(2,a):
      if a%i == 0:
         tru = 1
    if tru == 1:
       print("소수가 아닙니다.")
    else:
        print("소수입니다.")
else:
   print("소수가 아닙니다.")
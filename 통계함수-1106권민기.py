import math
lst = list(range(1,11))

#평균
mean =sum(lst)/len(lst)

print(f"평균:{mean}")

#분산 = 편차 제곱의 평균|편차 = 점수 - 평균
vsum = 0
for x in lst:
    vsum += (x - mean)**2
    var = vsum/len(lst)
print(var)

#표준편차 = 루트(분산)
std = math.sqrt(var)
print(f"표준편차:{std}")

#최대공약수,최소공배수
gcd = math.gcd(*lst)
lcm = math.lcm(*lst)
print(f"최대공약수:{gcd},최소공배수:{lcm}")
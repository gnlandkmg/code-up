import random
n1 = random.randint(1,10)
n2 = random.randint(1,10)
sum = 0
print(n1,n2)
if n1 == n2:
    print(n1)
elif n2<n1:
    for i in range(n2,n1+1):
        sum = sum + i
    print(sum)
else:
    for i in range(n1,n2+1):
        sum = sum + i
    print(sum)
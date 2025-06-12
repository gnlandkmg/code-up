n=int(input())
for i in range(n):
    for j in range(i):
        print(" ",end = "")
    for m in range(n-i):
        if m == n-i-1:
            print("*")
        else:
            print("*",end ="")
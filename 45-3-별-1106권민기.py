n = int(input())

for i in range(n-1,-1,-1):
    print(" "*i,end="")
    for j in range(0,n-i):
        if j == n-i-1:
            print("*")
        else:
            print("*",end = "")

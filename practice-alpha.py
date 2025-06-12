t = int(input())
for k in range(t):
    n = int(input())
    row = []
    for i in range(1,7):
        for j in range(1,7):
            if i+j == n:
                li = [i,j]
                row.append(li)
    print(f"Case {k+1}:")
    if len(row) %2 == 0:
        for m in range(len(row)//2):
            print(f"({row[m][0]},{row[m][1]})")
    else:
        for m in range(len(row)//2+1):
            print(f"({row[m][0]},{row[m][1]})")
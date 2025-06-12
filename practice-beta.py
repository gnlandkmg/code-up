t=int(input())
for i in range(t):
    li = list(input())
    n = []
    row = []
    for j in range(1,len(li)+1):
        n.append(int(li[-i]))
    for j in range(len(li)):
        num = 0
        num += int(li[i])
        num += n[i]
        row.append(num)
    e = 0
    for j in range(len(row)//2):
        if row[j] == row[-(j+1)]:
            e += 1
    if e == len(row)//2:
        print('YES')
    else:
        print("NO")
        
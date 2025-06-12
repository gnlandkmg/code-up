def get_data(a1,b1,a2,b2):
    a1,b1 = map(int,input().split())
    a2,b2 = map(int,input().split())
    return

def get_line(a1,b1,a2,b2):
    if a1 == a2:
        rst = a1
    else:
        slp = (b2-b1)/(a2 -a1)
        y_i = b1 - slp*a1
        rst = f'y = {slp}x + ({y_i})'
    return rst

x1,y1,x2,y2 = get_data()
line = get_line(x1,y1,x2,y2)
print(line)
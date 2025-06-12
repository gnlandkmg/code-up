f = open('data_1.txt','r')

while True:
    line=f.readline()
    if line =="":
        break
    else:
        print(line,end='')
f.close()
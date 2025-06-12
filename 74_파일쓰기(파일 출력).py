f = open('data_1.txt','r')

for i in range(1,11):
    line = "줄"
    f.write(f"{i}번째 {line}\n")

f.close()
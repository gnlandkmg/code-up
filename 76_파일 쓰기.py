f = open('data_2.txt',"w")

while True:
    content=input('내용입력:')
    if content == "":
        break
    else:
        f.write(f"{content}\n")
f.close()
import random,time

w = ['cat','dog','fox','monkey','mouse','panda','frog','snake','wolf']

start = time.time()
n = 0 #pass 개수
i=0 #문제 수
while True:
    keyword = random.choice(w)
    print(f"[문제 {i}]")
    print(keyword)
    player =  str(input())
    if player == keyword:
        print("pass")
        n = n +1
    else:
        print("fail")
    if n >= 5:
        stop = time.time()
        break
    i = i+1
print(f"걸린 시간: {stop-start}")
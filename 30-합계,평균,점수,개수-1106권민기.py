sum = 0
avg = 0
count = 0

while True:
    score = float(input("점수:"))
    if score == -1:
        break
    count = count+1
    sum = sum+score
avg = sum/count
print("="*10)
print(f"합계:{sum}")
print(f"평균:{avg}")
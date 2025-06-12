n = int(input())
a = list()
o = 1
x = 0#big
y = 1002#small
while 0 <= n:
	if o-1 == n:
		break
	a.append(int(input()))
	if a[-1] > x:
		x = a[-1]
	if a[-1] < y:
		y = a[-1]
	o= o + 1
print(f"최대값은 {x}, 최소값은 {y}")
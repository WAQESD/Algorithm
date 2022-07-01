from sys import stdin
n = int(stdin.readline())
p = list(map(int, stdin.readline().split()))
p.sort()

result = 4000000000
answer = []
for i in range(n-2):
	now = p[i]
	l = i+1
	r = n-1
	while(l < r):
		sum = now + p[l] + p[r]
		if(abs(sum) < result):
			result = abs(sum)
			answer = [now, p[l], p[r]]
		if(sum > 0): r -= 1
		elif(sum < 0): l += 1
		else: break
			
	if(result == 0): break
print(*answer)
from sys import stdin

n = int(stdin.readline())

k = (n * (n+1)) // 2
best = [0] * (k+1)
idx = 1
for i in range(n):
	v = list(map(int, stdin.readline().split()))
	for j in v:
		best[idx] = j
		idx += 1
cnt = 1
for i in range(2, n+1):
	for j in range(1, i+1):
		idx = cnt + j
		right = best[idx] + best[idx - i+1]
		left = best[idx] + best[idx - i]
		if(j == 1): 
			best[idx] = right
		elif(j == i): 
			best[idx] = left
		else: 
			best[idx] = max(left, right)
	cnt += i
print(max(best))

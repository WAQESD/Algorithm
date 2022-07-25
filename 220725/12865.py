from sys import stdin
n, k = map(int, stdin.readline().split())
items = []
dp = [0] * 100001
for i in range(n): items.append(list(map(int, stdin.readline().split())))
items.sort()
for [w, v] in items:
	for i in range(k-1, -1, -1):
		if(w+i > k): continue
		dp[w+i] = max(dp[w+i], dp[i]+v)
print(dp[k])
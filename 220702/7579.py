from sys import stdin
n, m = map(int, stdin.readline().split())
byte = [0] + list(map(int, stdin.readline().split()))
cost = [0] + list(map(int, stdin.readline().split()))
INF = sum(cost) + 1
result = INF
dp = [[0] * INF for _ in range(n+1)]
for i in range(1, n+1):
	b = byte[i]
	c = cost[i]
	for j in range(INF):
		if(j < c): dp[i][j] = dp[i-1][j]
		else: dp[i][j] = max(b + dp[i-1][j-c], dp[i-1][j])
		if(dp[i][j] >= m): result = min(result, j)

print(result)
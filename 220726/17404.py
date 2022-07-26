from sys import stdin
n = int(stdin.readline())
INF = 10**9
rgb = [list(map(int, stdin.readline().split())) for _ in range(n)]
dp = [[[INF] * 3 for _ in range(3)] for _ in range(n)]
for start in range(3):
	dp[0][start][start] = rgb[0][start]
	for i in range(1, n):
		for j in range(3):
			for k in range(3):
				if(j == k): continue
				dp[i][start][j] = min(dp[i][start][j], dp[i-1][start][k] + rgb[i][j])
answer = INF
for i in range(3):
	for j in range(3):
		if(i == j): continue
		answer = min(answer, dp[-1][i][j])
print(answer)			

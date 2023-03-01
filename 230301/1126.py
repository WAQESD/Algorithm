from sys import stdin

n = int(stdin.readline())
blocks = list(map(int, stdin.readline().split()))

dp = [[-1] * 500002 for _ in range(n+1)]

for i in range(1, n+1):
    dp[i][500001] = -9999999999

for i in range(500002):
	dp[0][i] = -9999999999
        
dp[0][0] = 0
    
for i in range(1, n+1):
    block = blocks[i-1]
    for j in range(500001):
        dp[i][j] = max(dp[i-1][j], dp[i-1][min(500001, j+block)], dp[i-1][abs(block-j)]+min(block, j))


print(dp[n][0])
			
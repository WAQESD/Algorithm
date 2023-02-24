from sys import stdin

s = stdin.readline()[:-1]
dp = [[0] * len(s) for _ in range(len(s))]

for i in range(len(s)):
	dp[i][i] = 1

for i in range(len(s)-1):
	dp[i][i+1] = 3 if s[i] == s[i+1] else 2

for gap in range(2, len(s)):
	for i in range(len(s)-gap):
		j = i + gap
		dp[i][j] += dp[i+1][j]
		dp[i][j] += dp[i][j-1]
		dp[i][j] -= dp[i+1][j-1]

		if s[i] == s[j]: dp[i][j] += dp[i+1][j-1] + 1

print(dp[0][len(s)-1])
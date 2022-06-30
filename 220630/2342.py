from sys import stdin
import sys
sys.setrecursionlimit(10**9)
INF = 10**9
action = list(map(int, stdin.readline().split()))[:-1]
cost = [[0]*5 for _ in range(5)]
for i in range(5):
	cost[i][i] = 1
	cost[0][i] = 2
	cost[i][0] = 2
for i in range(1, 4):
	cost[i][i+1] = 3
	cost[i+1][i] = 3
for i in range(1, 3):
	cost[i][i+2] = 4
	cost[i+2][i] = 4
cost[4][1] = 3
cost[1][4] = 3

dp = [[INF] * 25 for i in range(len(action))]

answer = 0
def dfs(l, r, n):
	if(n == len(action)): return 0
	if(dp[n][l*5+r] != INF): return dp[n][l*5+r]
	next = action[n]
	lc = cost[l][next] + dfs(next, r, n+1)
	rc = cost[r][next] + dfs(l, next, n+1)
	dp[n][l*5+r] = min(lc, rc)
	return dp[n][l*5+r]
print(dfs(0,0,0))

# 1 2 2 4 1 2 2 4 1 2 2 4 1 2 2 4 1 2 2 4 1 2 2 4 1 2 2 4 1 2 2 4 1 2 2 4 1 2 2 4 1 2 2 4 1 2 2 4 1 2 2 4 1 2 2 4 1 2 2 4 1 2 2 4 1 2 2 4 1 2 2 4 1 2 2 4 1 2 2 4 1 2 2 4 1 2 2 4 1 2 2 4 1 2 2 4 1 2 2 4 1 2 2 4 1 2 2 4 1 2 2 4 1 2 2 4 1 2 2 4 1 2 2 4 1 2 2 4 0
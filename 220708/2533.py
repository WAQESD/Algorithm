from sys import stdin
import sys
sys.setrecursionlimit(10 ** 9)
n = int(stdin.readline())
adj = [[] for _ in range(n+1)]
dp = [[0,0] for _ in range(n+1)]
visited = [0] * (n+1)
for i in range(n-1):
	u, v = map(int, stdin.readline().split())
	adj[u].append(v)
	adj[v].append(u)

def dfs(now):
	visited[now] = 1
	dp[now][0] = 1
	for next in adj[now]:
		if(visited[next] == 1): continue
		dfs(next)
		dp[now][0] += min(dp[next][0], dp[next][1])
		dp[now][1] += dp[next][0]

dfs(1)
print(min(dp[1][0], dp[1][1]))

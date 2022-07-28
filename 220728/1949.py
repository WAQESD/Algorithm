from sys import stdin
import sys
sys.setrecursionlimit(10**5+1)

n = int(stdin.readline())
people = [0] + list(map(int, stdin.readline().split()))
adj = [[] for _ in range(n+1)]
for i in range(n-1):
	a, b = map(int, stdin.readline().split())
	adj[a].append(b)
	adj[b].append(a)
visited = [0] * (n+1)
dp = [[0, 0] for _ in range(n+1)]
def dfs(now, prev):
	if(dp[now][prev] > 0): return dp[now][prev]
	result = 0
	for nxt in adj[now]:
		if(visited[nxt]): continue
		visited[nxt] = 1
		result += dfs(nxt, 0)
		visited[nxt] = 0
	if(not prev):
		tmp = people[now]
		for nxt in adj[now]:
			if(visited[nxt]): continue
			visited[nxt] = 1
			tmp += dfs(nxt, 1)
			visited[nxt] = 0
		result = max(result, tmp)
	dp[now][prev] = result
	return result

visited[1] = 1
result = dfs(1, 0)
print(result)
from sys import stdin
import sys
sys.setrecursionlimit(10**6)
n = int(stdin.readline())
maxLevel = 16
adj = [[] for _ in range(n+1)]
d = [0] * (n+1)
parents = [[[0, 0] for _ in range(maxLevel)] for _ in range(n+1)]
for i in range(n-1):
	s, e, t = map(int, stdin.readline().split())
	adj[s].append([e, t])
	adj[e].append([s, t])

root = 1
visited = [0]*(n+1)
visited[1] = 1
def dfs(now, depth):
	for [nxt, dist] in adj[now]:
		if(visited[nxt] == 1): continue
		visited[nxt] = 1
		parents[nxt][0] = [now, dist]
		d[nxt] = depth+1
		dfs(nxt, depth+1)
		visited[nxt] = 0
dfs(1, 0)

for i in range(1, maxLevel):
	for j in range(1, n+1):
		[parent, cost] = parents[j][i-1]
		parents[j][i] = [parents[parent][i-1][0], cost+parents[parent][i-1][1]]
m = int(stdin.readline())
for i in range(m):
	s, e = map(int, stdin.readline().split())
	result = 0

	if(d[s] > d[e]): s, e = e, s
	for i in range(maxLevel-1, -1, -1):
		if d[e] - d[s] >= (1 << i):
			result += parents[e][i][1]
			e = parents[e][i][0]
	if(s == e):
		print(result)
		continue
	for i in range(maxLevel-1, -1, -1):
		if parents[s][i][0] == 0 or parents[e][i][0] == 0: continue
		if parents[s][i][0] != parents[e][i][0]:
			result += parents[e][i][1]
			e = parents[e][i][0]
			result += parents[s][i][1]
			s = parents[s][i][0]
	result += parents[s][0][1]
	result += parents[e][0][1]
	print(result)
	

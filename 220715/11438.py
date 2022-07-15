from sys import stdin
import sys
sys.setrecursionlimit(10**5)
n = int(stdin.readline())
maxLevel = 21
adj = [[] for _ in range(n+1)]
d = [0] * (n+1)
parents = [[0]*maxLevel for _ in range(n+1)]
for i in range(n-1):
	s, e = map(int, stdin.readline().split())
	adj[s].append(e)
	adj[e].append(s)

root = 1
visited = [0]*(n+1)
def dfs(now, depth):
	visited[now] = 1
	d[now] = depth
	for nxt in adj[now]:
		if(visited[nxt] == 1): continue
		parents[nxt][0] = now
		dfs(nxt, depth+1)
dfs(1, 0)

for i in range(1, maxLevel):
	for j in range(1, n+1):
		parents[j][i] = parents[parents[j][i-1]][i-1]

def find(s, e):
	if(d[s] > d[e]): s, e = e, s
	for i in range(maxLevel-1, -1, -1):
		if d[e] - d[s] >= (1 << i):
			e = parents[e][i]
	if(s == e): return s
	for i in range(maxLevel-1, -1, -1):
		if parents[e][i] != parents[s][i]:
			e = parents[e][i]
			s = parents[s][i]
	return parents[s][0]

m = int(stdin.readline())
for i in range(m):
	s, e = map(int, stdin.readline().split())
	print(find(s,e))
	

from sys import stdin
import sys

sys.setrecursionlimit(200000)
V = int(stdin.readline())

tree = [[] for _ in range(V)]

for i in range(V-1):
	[s, e, t] = list(map(int, stdin.readline().split()))
	tree[s-1].append([e-1, t])
	tree[e-1].append([s-1, t])


maxdist = 0
maxidx = 0

visited = [0] * V
def dfs(now, x):
	global maxdist
	global maxidx
	visited[now] = 1
	if(x > maxdist):
		maxdist = x
		maxidx = now
	for [next, cost] in tree[now]:
		if(visited[next] == 1): continue
		dfs(next, x + cost)

dfs(0, 0)
visited = [0] * V
dfs(maxidx, 0)
print(maxdist)


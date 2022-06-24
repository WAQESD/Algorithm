from sys import stdin

V = int(stdin.readline())

tree = [[] for _ in range(V)]

for i in range(V):
	v = list(map(int, stdin.readline().split()))
	start = v[0] - 1
	for i in range(1, len(v) - 2, 2):
		tree[start].append([v[i] - 1, v[i+1]])

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


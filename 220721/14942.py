from sys import stdin
n = int(stdin.readline())
INF = 10**9
ants = []
roads = [[] for _ in range(n+1)]
parents = [-1] * (n+1)
d = [0] * (n+1)
for i in range(n): ants.append(int(stdin.readline()))
for i in range(n-1): 
	u, v, t = map(int, stdin.readline().split())
	roads[u].append([v, t])
	roads[v].append([u, t])

def dfs(now):
	for [nxt, t] in roads[now]:
		if(parents[nxt] > -1): continue
		parents[nxt] = now
		d[nxt] = t
		dfs(nxt)

def closest(now, e):
	if(now == 1): return now
	if(e >= d[now]) : return closest(parents[now], e - d[now])
	else: return now

parents[1] = 1
d[1] = 0
dfs(1)

for i in range(n):
	print(closest(i+1, ants[i]))
	
from sys import stdin
n, m = map(int, stdin.readline().split())
edges = [0] * m
parents = [i for i in range(n+1)]
cnt = 0
answer = 0
for i in range(m): 
	start, end, cost = map(int, stdin.readline().split())
	edges[i] = [cost, start, end]

edges.sort()

def getParent(node):
	if(parents[node] == node): return node
	return getParent(parents[node])

def union(s, e):
	if (s < e): parents[e] = s
	else: parents[s] = e

for [c, s, e] in edges:
	if (cnt == n-2): break
	sp = getParent(s)
	ep = getParent(e)
	if(sp == ep): continue
	union(sp,ep)
	cnt += 1
	answer += c

print(answer)
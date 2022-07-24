from sys import stdin
import sys
sys.setrecursionlimit(10**6)
v, E = map(int, stdin.readline().split())
adj = [[] for _ in range(v+1)]
parents = [0] * (v+1)
for i in range(E): 
	s, e = map(int, stdin.readline().split())
	adj[s].append(e)
	adj[e].append(s)
cnt = 1
answer = []
def dfs(now, prev):
	global cnt
	parents[now] = cnt
	ret = cnt
	cnt += 1
	for nxt in adj[now]:
		if(nxt == prev): continue
		if(parents[nxt] == 0): 
			parent = dfs(nxt, now)
			if(ret < parent): answer.append([min(now, nxt), max(now, nxt)])
			ret = min(ret, parent)
		else: ret = min(ret, parents[nxt])
	return ret

for i in range(1, v+1):
	dfs(i, 0)
answer.sort()
print(len(answer))
for [a, b] in answer:
	print(a,b)

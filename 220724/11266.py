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
answer = set()
def dfs(now, cnt):
	parents[now] = cnt
	ret = cnt
	children = 0
	for nxt in adj[now]:
		if(parents[nxt] == 0): 
			children += 1
			parent = dfs(nxt, cnt+1)
			if(cnt != 1 and parents[now] <= parent): answer.add(now)
			ret = min(ret, parent)
		else: ret = min(ret, parents[nxt])
	if(cnt == 1 and children >= 2): answer.add(now)
	return ret

for i in range(1, v+1):
	if(parents[i] == 0 and len(adj[i]) > 0):
		dfs(i, 1)
answer = list(answer)
answer.sort()
print(len(answer))
print(*answer)

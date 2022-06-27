from sys import stdin
import heapq
INF = int(10e9)
n, m, r = map(int, stdin.readline().split())
items = list(map(int, stdin.readline().split()))
d = [[INF] * n for _ in range(n)]
adj = [[] for _ in range(n)]
for i in range(r):
	s, e, t = map(int, stdin.readline().split())
	adj[s-1].append([e-1, t])
	adj[e-1].append([s-1, t])

def dij(start):
	d[start][start] = 0
	heap = [[0, start]]
	while(len(heap) > 0):
		[dist, now] = heapq.heappop(heap)
		if(dist > d[start][now]): continue
		for [next, cost] in adj[now]:
			nextD = dist + cost
			if(nextD < d[start][next]):
				d[start][next] = nextD
				heapq.heappush(heap,[nextD, next])
result = 0
for i in range(n): 
	dij(i)
	cnt = 0
	for j in range(n):
		if(d[i][j] <= m):
			cnt += items[j]
	result = max(result, cnt)
print(result)

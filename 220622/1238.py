import math
import heapq
from sys import stdin

[N, M, x] = list(map(int, stdin.readline().split()))
adj = [[] for _ in range(N)]
dist = [[math.inf] * N for _ in range(N)]
for i in range(M):
	[start, end, d] = list(map(int, stdin.readline().split()))
	adj[start-1].append([end-1, d])

def dij(start):
	dist[start][start] = 0
	heap = [[0, start]]
	while(len(heap) > 0):
		d = heap[0][0]
		now = heap[0][1]
		heapq.heappop(heap)
		if(dist[start][now] < d): continue
		for [next, cost] in adj[now]:
			nextD = d + cost
			if(nextD < dist[start][next]):
				dist[start][next] = nextD
				heapq.heappush(heap, [nextD, next])

answer = 0
for i in range(N): dij(i)
for i in range(N): answer = max(answer, dist[i][x-1] + dist[x-1][i])
print(answer)
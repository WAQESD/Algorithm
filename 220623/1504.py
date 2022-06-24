import math
import heapq
from sys import stdin

[N, E] = list(map(int, stdin.readline().split()))

adj = [[] for _ in range(N)]
d = [[math.inf] * N for _ in range(N)]

for i in range(E):
	[start, end, dist] = list(map(int, stdin.readline().split()))
	adj[start-1].append([end-1, dist])
	adj[end-1].append([start-1, dist])

[v1, v2] = list(map(int, stdin.readline().split()))
v1 -= 1
v2 -= 1

def dij(start):
	d[start][start] = 0
	heap = [[0, start]]
	while(len(heap) > 0):
		now = heap[0][1]
		dist = heap[0][0]
		heapq.heappop(heap)
		if(dist > d[start][now]): continue
		for [next, cost] in adj[now]:
			nextD = cost + dist
			if(nextD < d[start][next]):
				d[start][next] = nextD
				heapq.heappush(heap, [nextD, next])

dij(0)
dij(v1)
dij(v2)
answer1 = d[0][v1] + d[v1][v2] + d[v2][N-1]
answer2 = d[0][v2] + d[v2][v1] + d[v1][N-1]

answer = min(answer1, answer2)
if(answer == math.inf): print(-1)
else: print(answer)

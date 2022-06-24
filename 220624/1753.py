from sys import stdin
from math import inf
import heapq
[V, E] = list(map(int, stdin.readline().split()))
K = int(stdin.readline()) - 1
adj = [[] for _ in range(V)]
d = [ inf for _ in range(V)]
for i in range(E):
	[u, v, w] = list(map(int, stdin.readline().split()))
	adj[u-1].append([v-1, w])


def dij(start):
	d[start] = 0
	heap = [[0, start]]
	while(len(heap) > 0):
		now = heap[0][1]
		dist = heap[0][0]
		heapq.heappop(heap)
		if(dist > d[now]): continue
		for [next, cost] in adj[now]:
			nextD = dist + cost
			if(nextD < d[next]):
				d[next] = nextD
				heapq.heappush(heap, [nextD, next])
			
dij(K)
for i in range(V):
	if(d[i] == inf): print('INF')
	else: print(d[i])

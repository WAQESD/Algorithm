from sys import stdin
import math
import heapq

N = int(stdin.readline())
M = int(stdin.readline())
d = [math.inf] * N
bus = [[] for _ in range(N)]
for i in range(M):
	[s, e, t] = list(map(int, stdin.readline().split()))
	bus[s-1].append([e-1, t])

def dij(start):
	d[start] = 0
	heap = [[0, start]]
	while(len(heap) > 0):
		now = heap[0][1]
		dist = heap[0][0]
		heapq.heappop(heap)
		if(dist > d[now]): continue
		for [next, cost] in bus[now]:
			nextD = cost + dist
			if(nextD < d[next]):
				d[next] = nextD
				heapq.heappush(heap, [nextD, next])

[S, E] = list(map(int, stdin.readline().split()))

dij(S-1)
print(d[E-1])

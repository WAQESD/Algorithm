from sys import stdin
from math import inf
import heapq

TC = int(stdin.readline())
for i in range(TC):
	[N, M, W] = list(map(int, stdin.readline().split()))
	go = [[] for _ in range(N)]
	d = [[inf] * N for _ in range(N)]
	y = False
	for j in range(M):
		[S, E, T] = list(map(int, stdin.readline().split()))
		go[S-1].append([E-1, T])
		go[E-1].append([S-1, T])

	def dij(start):
		d[start][start] = 0

		heap = [[0, start]]
		while(len(heap)):
			now = heap[0][1]
			dist = heap[0][0]
			heapq.heappop(heap)
			if(dist > d[start][now]): continue
			for [next, cost] in go[now]:
				nextD = dist + cost
				if(nextD < d[start][next]):
					d[start][next] = nextD
					heapq.heappush(heap, [nextD, next])

	wormhole = []
	for j in range(W):
		[S, E, T] = list(map(int, stdin.readline().split()))
		d[S-1][E-1] = -T
		wormhole.append([S,E,T])
	for j in range(N): dij(j)
	print(d)
	for [S,E,T] in wormhole:
		if(T > d[E-1][S-1]): y = True
	if(y): print('YES')
	else: print('NO')


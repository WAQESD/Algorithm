from sys import stdin
import heapq
INF = 10**9
n, m, k = map(int, stdin.readline().split())
start, end = map(int, stdin.readline().split())
adj = [[] for _ in range(n+1)]
for i in range(m):
	s, e, t = map(int, stdin.readline().split())
	adj[s].append((e, t))
	adj[e].append((s, t))
tax = [0]
for i in range(k): tax.append(int(stdin.readline()))
def dij(start):
	d = [[INF] * (n+1) for _ in range(n+1)]
	d[start][0] = 0
	heap = [(0, start, 0)]
	while(heap):
		dist, now, cnt = heapq.heappop(heap)
		check = False
		for i in range(cnt+1):
			if d[now][i] < dist:
				check = True
				break
		if(check or cnt >= n): continue
		for nxt, cost in adj[now]:
			nextDist = cost + dist
			if(nextDist < d[nxt][cnt+1]):
				d[nxt][cnt+1] = nextDist
				heapq.heappush(heap, (nextDist, nxt, cnt+1))
	return d[end]
d = dij(start)
for i in range(k+1):
	for j in range(n): 
		d[j] = d[j] + tax[i] * j
	print(min(d))

from collections import deque
import heapq
from sys import stdin

while True:
	n, m = map(int, stdin.readline().split())
	if(n == 0 and m==0): break
	start, end = map(int, stdin.readline().split())
	go = [[] for _ in range(n)]
	back = [[] for _ in range(n)]
	check = [[False]*n for _ in range(n)]
	for i in range(m):
		u, v, p = map(int, stdin.readline().split())
		go[u].append([v, p])
		go[v].append([u, p])
		check[u][v] = True

	def dij(start, end, edges):
		heap = [[0, start]]
		d = [float('inf')] * n
		visited = [False] * n
		while heap:
			[dist, now] = heapq.heappop(heap)
			if visited[now]: continue
			visited[now] = True
			if dist > d[now]: continue
			d[now] = dist
			if now == end: return d
			for [nxt, cost] in edges[now]:
				nd = dist + cost
				if nd > d[nxt] or not check[now][nxt]: continue
				heapq.heappush(heap, [nd, nxt])
		
	dist1 = dij(start, end, go)
	if dist1 == None:
		print(-1)
		continue
	shortest = dist1[end]

	q = deque()
	q.append([0, end])
	while q:
		[dist, now] = q.popleft()
		for [nxt, cost] in back[now]:
			nd = dist + cost
			if nd + dist1[nxt] == shortest:
				if check[nxt][now]:
					check[nxt][now] = False
					q.append([nd, nxt])
	answer = dij(start, end, go)

	print(answer[end] if answer != None else -1)


from sys import stdin
import heapq
n, m = map(int, stdin.readline().split())
adjm = [[0] * (n+1) for _ in range(n+1)]
adjM = [[101] * (n+1) for _ in range(n+1)]
for _ in range(m):
	s, e, l = map(int, stdin.readline().split())
	adjM[s][e] = max(l, adjM[s][e])
	adjM[e][s] = max(l, adjM[e][s])
	adjm[s][e] = min(l, adjm[s][e])
	adjm[e][s] = min(l, adjm[e][s])

def bfs(start):
	heap = [[0, start]]
	visited = [0] * (n+1)
	last = []
	while(heap):
		now = heapq.heappop(heap)
		stack = [now[1]]
		t = now[0]
		while(heap[0][0] == t):
			stack.append(heapq.heappop(heap)[1])
		last = stack
		for next in stack:
			if(visited[next] == 1): continue
			visited[next] = 1
			for i in range(1, n+1):
				if(visited[i] == 1): continue
				heapq.heappush(heap, [adjm[]])
	


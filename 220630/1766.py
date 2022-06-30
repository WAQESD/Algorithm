from sys import stdin
import heapq
N, M = map(int, stdin.readline().split())
adj = [[] for _ in range(N+1)]
arr = [0] * (N+1)
for i in range(M):
	a, b = map(int, stdin.readline().split())
	adj[a].append(b)
	arr[b]+=1
heap = []
for i in range(1, N+1):
	if(arr[i] == 0): heapq.heappush(heap, i)
while(len(heap)):
	now = heapq.heappop(heap)
	print(now, end=" ")
	for i in adj[now]:
		arr[i] -= 1
		if(arr[i] == 0): heapq.heappush(heap, i)

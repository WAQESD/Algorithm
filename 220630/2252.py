from sys import stdin
from collections import deque
N, M = map(int, stdin.readline().split())
adj = [[] for _ in range(N+1)]
arr = [0] * (N+1)
for i in range(M):
	a, b = map(int, stdin.readline().split())
	adj[a].append(b)
	arr[b]+=1
q = deque()
for i in range(1, N+1):
	if(arr[i] == 0): q.append(i)
while(len(q)):
	now = q.popleft()
	print(now, end=" ")
	for i in adj[now]:
		arr[i] -= 1
		if(arr[i] == 0): q.append(i)
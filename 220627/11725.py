from sys import stdin
from collections import deque
n = int(stdin.readline())
adj = [[] for _ in range(n)]
parents = [-1] * n
parents[0] = 0
for i in range(n-1):
	a, b = map(int, stdin.readline().split())
	adj[a-1].append(b-1)
	adj[b-1].append(a-1)
q = deque()
q.append(0)
while(len(q) > 0):
	parent = q.popleft()
	for next in adj[parent]:
		if(parents[next] < 0):
			parents[next] = parent
			q.append(next)
for i in range(1,n):
	print(parents[i] + 1)

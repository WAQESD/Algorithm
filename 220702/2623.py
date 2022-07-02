from sys import stdin
from collections import deque
n, m = map(int, stdin.readline().split())

adj = [set() for _ in range(n+1)]
for i in range(m):
	l = list(map(int, stdin.readline().split()))[1:]
	for j in range(len(l)-1):
		for k in range(j+1, len(l)):
			adj[l[k]].add(l[j])

q = deque()
for i in range(1,n+1):
	if(len(adj[i]) == 0): q.append(i)

visited = [0] * (n+1)
answer = []
while(len(q)):
	now = q.popleft()
	if(visited[now] == 1): continue
	visited[now] = 1
	answer.append(now)
	for i in range(1,n+1):
		adj[i] = adj[i] - set([now])
		if(len(adj[i]) == 0): q.append(i)
if(len(answer) < n): print(0)
else:
	for i in range(n):
		print(answer[i])

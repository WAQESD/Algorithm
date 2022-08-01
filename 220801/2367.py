from sys import stdin
from collections import deque
n, k, d = map(int, stdin.readline().split())
INF = int(1e9)
limit = list(map(int, stdin.readline().split()))
line = [[] for _ in range(n+d+3)]
flow = [[0] * (n+d+3) for _ in range(n+d+3)]
capacity = [[0] * (n+d+3) for _ in range(n+d+3)]
for i in range(3, n+3):
	line[1].append(i)
	line[i].append(1)
	capacity[1][i] = k

for i in range(n+3, n+d+3):
	line[i].append(2)
	line[2].append(i)
	capacity[i][2] = limit[i-n-3]

for i in range(3, n+3):
	for food in list(map(int, stdin.readline().split()))[1:]:
		line[i].append(n+2+food)
		line[n+2+food].append(i)
		capacity[i][n+2+food] = 1

def maxFlow(start, end):
	answer = 0
	while(True):
		parent = [0] * (n+d+3)
		q = deque()
		q.append(start)
		while(q and not parent[end]):
			now = q.popleft()
			for nxt in line[now]:
				if(capacity[now][nxt] - flow[now][nxt] <= 0 or parent[nxt]): continue
				q.append(nxt)
				parent[nxt] = now
		if(not parent[end]): break
		amount = INF
		idx = end
		while(idx != start): 
			amount = min(amount, capacity[parent[idx]][idx] - flow[parent[idx]][idx])
			idx = parent[idx]

		idx = end
		while(idx != start): 
			flow[parent[idx]][idx] += amount
			flow[idx][parent[idx]] -= amount
			idx = parent[idx]
		answer += amount
	return answer

print(maxFlow(1, 2))
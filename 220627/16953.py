from sys import stdin
from collections import deque
a, b = map(int, stdin.readline().split())

def bfs():
	q = deque()
	q.append([b, 1])
	while(len(q) > 0):
		[x, cnt] = q.popleft()
		if(x == a): return cnt
		if(x < a): continue
		if(x % 2 == 0): q.append([x//2, cnt+1])
		if(x % 10 == 1): q.append([x//10, cnt+1])
	return -1

print(bfs())

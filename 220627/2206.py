from sys import stdin
from collections import deque

N, M = map(int, stdin.readline().split())

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

m = [''] * N
for i in range(N): 
	v = stdin.readline()[:-1]
	m[i] = v

def bfs():
	visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
	visited[0][0][0] = 1
	q = deque()
	q.append([0,0,0])
	while(len(q) > 0):
		[x, y, z] = q.popleft()
		if(x == M-1 and y == N-1):return visited[y][x][z]
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			if(nx < 0 or nx >= M or ny < 0 or ny >= N): continue
			if(m[ny][nx] == '1' and z == 0):
				visited[ny][nx][1] = visited[y][x][0] + 1
				q.append((nx, ny, 1))
			elif(m[ny][nx] == '0' and visited[ny][nx][z] == 0):
				visited[ny][nx][z] = visited[y][x][z] + 1
				q.append((nx, ny, z))
	return -1
print(bfs())

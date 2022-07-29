from sys import stdin
from collections import deque
tc = int(stdin.readline())
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
for _ in range(tc):
	h, w = map(int,stdin.readline().split())
	m = [list('.'*(w+2))]
	for i in range(h): m.append(list('.' + stdin.readline().rstrip() + '.'))
	m.append(list('.'*(w+2)))
	prisoners = []
	for y in range(h+2):
		for x in range(w+2):
			if(m[y][x] == '$'): 
				m[y][x] = '.'
				prisoners.append([x, y])
	def bfs(x, y):
		visited = [[-1] * (w+2) for _ in range(h+2)]
		visited[y][x] = 0
		q = deque()
		q.append([x, y])
		while(q):
			[x, y] = q.popleft()
			for i in range(4):
				nx = x + dx[i]
				ny = y + dy[i]
				if(nx < 0 or nx >= w+2 or ny < 0 or ny >= h+2 or visited[ny][nx] > -1): continue
				if(m[ny][nx] == '.'):
					visited[ny][nx] = visited[y][x]
					q.appendleft([nx, ny])
				elif(m[ny][nx] == '#'):
					visited[ny][nx] = visited[y][x] + 1
					q.append([nx, ny])
		return visited
	sg = bfs(0,0)
	[a, b] = [bfs(x, y) for [x, y] in prisoners]
	answer = w * h
	for y in range(h+2):
		for x in range(w+2):
			if a[y][x] == -1 or b[y][x] == -1 or sg[y][x] == -1 or m[y][x] == '*': continue
			result = a[y][x] + b[y][x] + sg[y][x]
			if(m[y][x] == '#'): result -= 2
			answer = min(answer, result)
	print(answer)

from sys import stdin
from collections import deque

tc = int(stdin.readline())
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(tc):
	h, w = map(int, stdin.readline().split())
	m = []
	for i in range(h):
		line = list(stdin.readline().strip())
		m.append(line)
	keys = [0] * 26
	doors = [[] for _ in range(26)]
	key = list(stdin.readline().strip())
	visited = [[0] * w for _ in range(h)]
	result = 0
	for k in key:
		if(k == '0'): break
		keys[ord(k) - ord('a')] = 1
	
	q = deque()
	for i in range(w):
		if(m[0][i] != '*'): q.append([0, i])
		if(m[h-1][i] != '*'): q.append([h-1, i])
	for i in range(1, h-1):
		if(m[i][0] != '*'): q.append([i, 0])
		if(m[i][w-1] != '*'): q.append([i, w-1])

	while(len(q)):
		[y, x] = q.popleft()
		if(visited[y][x] == 1): continue
		if(ord('a') <= ord(m[y][x]) <= ord('z')):
			keys[ord(m[y][x])-ord('a')] = 1
			candi = doors[ord(m[y][x])-ord('a')]
			if(len(candi) > 0):
				for [ny, nx] in candi:
					q.append([ny, nx])
		elif(ord('A') <= ord(m[y][x]) <= ord('Z')):
			if(keys[ord(m[y][x]) - ord('A')] == 0):
				doors[ord(m[y][x]) - ord('A')].append([y, x])
				continue
		elif(m[y][x] == '$'): result += 1
		visited[y][x] = 1
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			if(nx < 0 or ny < 0 or nx >= w or ny >= h or m[ny][nx] == '*' or visited[ny][nx] == 1): continue
			q.append([ny, nx])
	print(result)

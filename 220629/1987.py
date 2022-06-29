from sys import stdin
R, C = map(int, stdin.readline().split())
lines = []
for i in range(R): lines.append(stdin.readline()[:-1])
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

visited = [0] * 26
A = ord('A')

def dfs(x, y, cnt):
	if(x == C-1 and y == R-1): return cnt
	result = cnt
	for i in range(4):
		nx = x + dx[i]
		ny = y + dy[i]
		if(nx < 0 or ny < 0 or nx >= C or ny >= R): continue
		pos = ord(lines[ny][nx]) - A
		if(visited[pos] == 1): continue
		visited[pos] = 1
		result = max(result, dfs(nx, ny, cnt+1))
		visited[pos] = 0

	return result

visited[ord(lines[0][0]) - A] = 1
print(dfs(0, 0, 1))

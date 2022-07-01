from sys import stdin
n, m = map(int, stdin.readline().split())
visited = [[0 for j in range(m)] for i in range(n)]
arr = []
for i in range(n): arr.append(stdin.readline()[:-1])

def move(y, x):
	if(arr[y][x] == 'D'): return [y+1, x]
	if(arr[y][x] == 'U'): return [y-1, x]
	if(arr[y][x] == 'R'): return [y, x+1]
	if(arr[y][x] == 'L'): return [y, x-1]

def find(ny, nx):
	id = ny*m+nx
	stack = [id]
	visited[i][j] = 1
	while(len(stack)):
		ny , nx = move(ny, nx)
		id = ny * m + nx
		if(id in stack): break
		if(visited[ny][nx] == 1): return 0
		visited[ny][nx] = 1
		stack.append(id)
	return 1

answer = 0
for i in range(n):
	for j in range(m):
		if(visited[i][j] == 1): continue
		answer += find(i, j)

print(answer)

"""
3 4
RLRL
RLRL
RRRU
"""
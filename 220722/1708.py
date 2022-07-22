from sys import stdin
n = int(stdin.readline())
points = []
visited = [0] * n
for i in range(n): points.append(list(map(int, stdin.readline().split())))

def ccw(a, b, c):
	return (b[0] - a[0]) * (c[1] - a[1]) - (c[0] - a[0]) * (b[1] - a[1])

def dfs(prev, now, cnt):
	for i in range(n):
		if(visited[i]): continue
		dfs(now, i, cnt+1)

from sys import stdin
n = int(stdin.readline())
w = int(stdin.readline())
tasks = [[1,1], [n, n]]
for i in range(w): tasks.append(list(map(int, stdin.readline().split())))
def dist(a, b):
	return abs(a[0] - b[0]) + abs(a[1] - b[1])
dp = [[-1] * (w+3) for _ in range(w+3)]
answer = [[-1] * (w+3) for _ in range(w+3)]

def police(a, b):
	now = max(a, b) + 1
	if(now == w+2): return 0
	if(dp[a][b] > -1): return dp[a][b]
	one = police(now, b) + dist(tasks[a], tasks[now])
	two = police(a, now) + dist(tasks[b], tasks[now])
	if(one < two): answer[a][b] = 1
	else: answer[a][b] = 2
	dp[a][b] = min(one, two)
	return dp[a][b]

print(police(0, 1))

x = 0
y = 1
while(x < w+1 and y < w+1):
	print(answer[x][y])
	if(answer[x][y] == 1): x = max(x, y)+1
	else: y = max(x, y)+1


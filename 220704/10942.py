from sys import stdin
n = int(stdin.readline())
line = [-1] + list(map(int, stdin.readline().split()))
q = int(stdin.readline())
cache = [[0] * (n+1) for _ in range(n+1)]
for i in range(1, n+1): cache[i][i] = 1
for i in range(1, n):
	if(line[i] == line[i+1]): cache[i][i+1] = 1
for i in range(2, n+1):
	for j in range(1, n+1-i):
		if(cache[j+1][j+i-1] == 1 and line[j] == line[j+i]): cache[j][j+i] = 1
		
for i in range(q):
	s, e = map(int, stdin.readline().split())
	print(cache[s][e])

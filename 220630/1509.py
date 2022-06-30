line = input()
n = len(line)
INF = 10**9
cache = [[0] * n for _ in range(n)]
result = [INF] * (n+1)
result[0] = 0
for i in range(n): cache[i][i] = 1
for i in range(n-1): 
	if(line[i] == line[i+1]): cache[i][i+1] = 1

for i in range(2, n):
	for j in range(n-i):
		if(line[j] == line[j+i] and cache[j+1][j+i-1] == 1): cache[j][j+i] = 1

for i in range(1, n+1):
	result[i] = min(result[i], result[i-1] + 1)
	for j in range(i+1, n+1):
		if(cache[i-1][j-1] != 0): result[j] = min(result[j], result[i-1] + 1)

print(result[n])
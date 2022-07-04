from sys import stdin
n = int(stdin.readline())
dp = [[0] * n for _ in range(n)]
matrix = []
for i in range(n):
	r, c = map(int, stdin.readline().split())
	matrix.append([r,c])

def dfs(start, end):
	if(dp[start][end] > 0): return dp[start][end]
	if(end - start == 1): 
		dp[start][end] = matrix[start][0] * matrix[start][1] * matrix[end][1]
		return dp[start][end]
	result = min(matrix[start][0] * matrix[start][1] * matrix[end][1] + dfs(start+1, end), dfs(start, end-1) + matrix[start][0] * matrix[end][0] * matrix[end][1])
	for i in range(start+1, end-1):
		result = min(result, dfs(start, i) + dfs(i+1, end) + matrix[start][0] * matrix[i][1] * matrix[end][1])
	dp[start][end] = result
	return dp[start][end]

print(dfs(0, n-1))
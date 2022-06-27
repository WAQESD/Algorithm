from sys import stdin
n, m = map(int, stdin.readline().split())
arr = [[0] * (n+1) for _ in range(n+1)]
for i in range(1, n+1):
	arr[i][i] = 1
	arr[i][0] = 1

def rec(n, m):
	if(arr[n][m] > 0): return arr[n][m]
	arr[n][m] = rec(n-1, m) + rec(n-1, m-1)
	return arr[n][m]

print(rec(n,m))
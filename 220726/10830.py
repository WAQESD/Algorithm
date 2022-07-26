from sys import stdin
n, b = map(int,stdin.readline().split())
matrix = [list(map(int, stdin.readline().split())) for _ in range(n)]
def mul(a, b):	
	new = [[0] * n for _ in range(n)]
	for i in range(n):
		for j in range(n):
			for k in range(n):
				new[i][j] += a[i][k] * b[k][j] % 1000
			new[i][j] %= 1000
	return new
	
def solve(mat, b):
	if(b == 1): return mat
	if(b == 2): return mul(mat, mat)
	if(b % 2):
		nxt = mul(mat, mat)
		return mul(solve(nxt, b//2), mat) 
	else:
		nxt = mul(mat, mat)
		return solve(nxt, b//2)

answer = solve(matrix, b)
for i in range(n):
	for j in range(n):
		print(answer[i][j] % 1000, end = " ")
	print()
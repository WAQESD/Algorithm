from sys import stdin
n, m = map(int, stdin.readline().split())
mat = [[0] * (n) for _ in range(n)]

for i in range(m):
	a, b = map(int, stdin.readline().split())
	mat[a-1][b-1] = 1
	mat[b-1][a-1] = 1

def mul(a, b):
	result = [[0] * (n) for _ in range(n)]
	for i in range(n):
		for j in range(n):
			for k in range(n):
				result[i][j] += a[i][k] * b[k][j]
			result[i][j] %= 1000000007
	return result

D = int(stdin.readline())

def pow(a, k):
	if(k == 1): return a
	tmp = pow(a, k//2)
	result = mul(tmp, tmp)
	if(k % 2 == 1): result = mul(result, a)
	return result

answer = pow(mat, D)
print(answer[0][0])
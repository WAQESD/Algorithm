from sys import stdin
n, s, e, t = map(int, stdin.readline().split())
mat = [[0] * (n*5) for _ in range(n*5)]

for i in range(n):
	for j in range(1,5):
		mat[i*5+j][i*5+j-1] = 1

for i in range(n):
	line = stdin.readline()[:-1]
	for j in range(n):
		cost = int(line[j])
		if(cost > 0): mat[i*5][j*5+cost-1] = 1

def mul(a, b):
	result = [[0] * (n*5) for _ in range(n*5)]
	for i in range(n*5):
		for j in range(n*5):
			for k in range(n*5):
				result[i][j] += a[i][k] * b[k][j]
			result[i][j] %= 1000003
	return result

def pow(a, k):
	if(k == 1): return a
	tmp = pow(a, k//2)
	result = mul(tmp, tmp)
	if(k % 2 == 1): result = mul(result, a)
	return result

answer = pow(mat, t)
print(answer)
print(answer[(s-1)*5][(e-1)*5])
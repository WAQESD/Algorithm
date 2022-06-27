from sys import stdin
tc = int(stdin.readline())
for i in range(tc):
	n = int(stdin.readline())
	a = list(map(int, stdin.readline().split()))
	b = list(map(int, stdin.readline().split()))
	result = [[0, 0] for _ in range(n)]
	result[0][0] = a[0]
	result[0][1] = b[0]
	for j in range(1,n):
		if(j == 1):
			result[j][0] = a[j] + result[j-1][1]
			result[j][1] = b[j] + result[j-1][0]
		else:
			result[j][0] = a[j] + max(result[j-1][1], result[j-2][1])
			result[j][1] = b[j] + max(result[j-1][0], result[j-2][0])
	print(max(result[n-1]))

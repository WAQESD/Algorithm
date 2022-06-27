from sys import stdin
n = int(stdin.readline())
m = [0,0,0]
M = [0,0,0]
for i in range(n):
	[a,b,c] = list(map(int,stdin.readline().split()))
	m = [a + min(m[:2]), b + min(m), c + min(m[1:])]
	M = [a + max(M[:2]), b + max(M), c + max(M[1:])]

print(str(max(M)) + ' ' + str(min(m)))

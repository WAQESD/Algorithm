from sys import stdin
inf = int(1e9)

TC = int(stdin.readline())
for i in range(TC):
	[N, M, W] = list(map(int, stdin.readline().split()))
	V = []
	for j in range(M):
		[S,E,T] = list(map(int, stdin.readline().split()))
		V.append([S,E,T])
		V.append([E,S,T])

	for j in range(W):
		[S, E, T] = list(map(int, stdin.readline().split()))
		V.append([S,E,-T])

	def bf(start):
		d = [inf] * (N+1) 
		d[start] = 0
		for i in range(1, N+1):
			for [S, E, T] in V:
				if(d[E] > d[S] + T):
					d[E] = d[S] + T
					if(i == N): return True

		return False
	result = bf(1)

	if(result): print('YES')
	else: print('NO')

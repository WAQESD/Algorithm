from sys import stdin
import sys
sys.setrecursionlimit(10**9)

tc = int(stdin.readline())
for _ in range(tc):
	n = int(stdin.readline())
	s = list(map(int, stdin.readline().split()))
	s = [x-1 for x in s]
	check = [0] * n
	answer = 0
	stack = []
	def dfs(now):
		stack.append(now)
		check[now] = 1
		next = s[now]
		if(check[next] == 1):
			if(next in stack): return stack.index(next)
			else: return len(stack)
		else:
			return dfs(next)

	for i in range(n):
		if(check[i] == 1): continue
		stack = []
		answer += dfs(i)

	print(answer)

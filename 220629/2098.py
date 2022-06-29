from sys import stdin
INF = 10**9
n = int(stdin.readline())
cost = []
for i in range(n): cost.append(list(map(int, stdin.readline().split())))
cache = [[0] * (2**n) for _ in range(n)]
def tsp(now, visited):
	if(visited == (1 << n)-1): 
		if(cost[now][0] > 0): return cost[now][0]
		else: return INF
	if(cache[now][visited] > 0): return cache[now][visited]
	result = INF
	for next in range(n):
		if(visited & (1 << next)): continue
		if(cost[now][next] == 0): continue
		result = min(result, tsp(next, visited | (1 << next)) + cost[now][next])
	cache[now][visited] = result
	return result

print(tsp(0, 1))
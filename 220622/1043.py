[N, M] = [int(x) for x in input().split(' ')]
D = [int(x) for x in input().split(' ')][1:]
T = set(D)
ll = [set() for _ in range(N)]
answer = 0
party = []

for i in range(M):
	P = [int(x) for x in input().split(' ')][1:]
	party.append(P)
	t = False
	for p in P: 
		if (p in T): 
			t = True
			break
	for i in range(len(P)):
		for j in range(i, len(P)):
			ll[P[i]-1].add(P[j])
			ll[P[j]-1].add(P[i])

def dfs(now):
	T.add(now)
	for next in ll[now-1]:
		if(next not in T):
			dfs(next)

for d in D:
	dfs(d)

for P in party:
	t = True
	for p in P:
		if(p in T): 
			t = False
			break
	if(t): answer += 1

print(answer)


"""
8 5
1 1
2 1 2
2 2 3
2 3 4
2 4 5
2 5 6
"""
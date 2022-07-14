from sys import stdin
import sys
sys.setrecursionlimit(10**9)
v, e = map(int, stdin.readline().split())
adj = [[] for _ in range(v+1)]
back = [[] for _ in range(v+1)]
for i in range(e):
	a, b = map(int, stdin.readline().split())
	adj[a].append(b)
stack = []
scc = []
ids = [0] * (v+1)
lo = [0] * (v+1)
check = [0] * (v+1)
id = 1
def SCC(now):
	global id
	stack.append(now)
	ids[now] = id
	lo[now] = id
	check[now] = 1
	id += 1
	for nxt in adj[now]:
		if(ids[nxt] == 0): 
			SCC(nxt)
			lo[now] = min(lo[now], lo[nxt])
		elif(check[nxt] == 1): lo[now] = min(lo[now], ids[nxt])
	if(ids[now] == lo[now]):
		cur_scc = []
		while True:
			top = stack.pop()
			cur_scc.append(top)
			check[top] = 0
			if(top == now): break
		cur_scc.sort()
		scc.append([cur_scc[0], cur_scc])

for i in range(1, v+1):
	if(ids[i] == 0): SCC(i)

scc.sort()
print(len(scc))
for [_,s] in scc: print(*s, -1)

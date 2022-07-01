from sys import stdin
n, m = map(int, stdin.readline().split())
v = []
for i in range(m):
	a, b = map(int, stdin.readline().split())
	v.append([a,b])
parents = [i for i in range(n+1)]

def getParent(x):
	if(x == parents[x]): return x
	return getParent(parents[x])

def union(x, y):
	px = getParent(x)
	py = getParent(y)
	if(px < py): parents[py] = px
	else: parents[px] = py

def answer():
	for i in range(m):
		[a, b] = v[i]
		if(getParent(a) == getParent(b)): return(i+1)
		union(a, b)
	return 0

print(answer())

from sys import stdin
G = int(stdin.readline())
P = int(stdin.readline())
arr = [0] * P
parents = [i for i in range(G+1)]
for i in range(P):
	g = int(stdin.readline())
	arr[i] = g

def find_parent(v):
	if(parents[v] == v): return v
	parents[v] = find_parent(parents[v])
	return parents[v]

answer = 0
for v in arr:
	x = find_parent(v)
	if(x == 0): break
	parents[x] = find_parent(x-1)
	answer += 1

print(answer)
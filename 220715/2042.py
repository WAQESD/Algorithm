from sys import stdin
n, m, k = map(int, stdin.readline().split())
tree = [0] * (n*4)
arr = []

def init(start, end, node):
	if(start == end):
		tree[node] = arr[start-1]
		return tree[node]
	mid = (start + end) // 2
	tree[node] = init(start, mid, node*2) + init(mid+1, end, node*2+1)
	return tree[node]

def update(node, start, end, v, index):
	if(index < start or index > end): return
	tree[node] += v
	if(start != end):
		mid = (start + end) // 2
		update(node*2, start, mid, v, index)
		update(node*2+1, mid+1, end, v, index)

def get(node, start, end, left, right):
	if(left > end or right < start): return 0
	if(start >= left and right >= end): return tree[node]
	mid = (start + end) // 2
	return get(2*node, start, mid, left, right) + get(2*node+1, mid+1, end, left, right)

for i in range(n): arr.append(int(stdin.readline()))

init(1, n, 1)

for i in range(m+k):
	[a, b, c] = list(map(int, stdin.readline().split()))
	if(a == 1): 
		update(1, 1, n, c - arr[b-1], b)
		arr[b-1] = c
	else: print(get(1, 1, n, b, c))
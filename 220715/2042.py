from sys import stdin
n, m, k = map(int, stdin.readline().split())
tree = [0] * (n*4)
arr = [0]
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
	return get(2*n, start, mid, left, right) + get(2*n+1, mid+1, end, left, right)

for i in range(1, n+1): 
	x = int(stdin.readline())
	arr.append(x)
	update(1, 1, n, x, i)

for i in range(m+k):
	[a, b, c] = list(map(int, stdin.readline().split()))
	if(a == 1): 
		update(1, 1, n, c - arr[b], b)
		arr[b] = c
	else: print(get(1, 1, n, b, c))
		

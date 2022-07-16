from sys import stdin
import math
tc = int(stdin.readline())
for i in range(tc):
	n, m  = map(int, stdin.readline().split())
	h = math.ceil(math.log2(n+m+1))
	size = 1 << (h+1)
	tree = [0] * (size+1)
	idx = list(range(n+1, 0, -1))

	def init(node, start, end):
		if(start == end): 
			tree[node] = 1
			return tree[node]
		mid = (start + end) // 2
		tree[node] = init(node*2, start, mid) + init(node*2+1, mid+1, end)
		return tree[node]

	def update(node, start, end, index, v):
		if(index < start or index > end): return
		tree[node] += v
		if(start != end):
			mid = (start + end) // 2
			update(node*2, start, mid, index, v)
			update(node*2+1, mid+1, end, index, v)

	def get(node, start, end, left, right):
		if(start > right or end < left): return 0
		if(start >= left and end <= right): return tree[node]
		mid = (start + end) // 2
		return get(node*2, start, mid, left, right) + get(node*2+1, mid+1, end, left, right)

	init(1, 1, n+m)
	cnt = 1
	for movie in map(int, stdin.readline().split()):
		now = idx[movie]
		idx[movie] = n+cnt
		print(get(1, 1, n+m, now+1, n+cnt-1), end = ' ')
		update(1, 1, n+m, now, -1)
		cnt += 1
	print()

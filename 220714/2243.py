from sys import stdin
M = 100000
n = int(stdin.readline())
tree = [0] * (M*4+10)
box = [0] * (M+1)

def update(node, start, end, diff, index):
	if(index < start or index > end): return
	tree[node] += diff
	if(start != end):
		mid = (start+end)//2
		update(node*2, start, mid, diff, index)
		update(node*2+1, mid+1, end, diff, index)

def takeOut(node, start, end, seq):
	if(start == end): return start
	mid = (start+end)//2
	if(tree[node*2] >= seq): return takeOut(node*2, start, mid, seq)
	else: return takeOut(node*2+1, mid+1, end, seq - tree[node*2])

for i in range(n):
	arr = list(map(int, stdin.readline().split()))
	a = arr[0]
	if(a == 2):
		[b, c] = arr[1:]
		box[b] += c
		update(1, 1, M, c, b)
	else:
		[b] = arr[1:]
		result = takeOut(1, 1, M, b)
		print(result)
		box[result] -= 1
		update(1, 1, M, -1, result)
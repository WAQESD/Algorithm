from sys import stdin
m = 1000000
n = int(stdin.readline())
tree = [0] * (m*4)
box = [0] * (m+1)

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
		box[arr[1]] += arr[2]
		update(1, 1, m, arr[2], arr[1])
	else:
		result = takeOut(1, 1, m, arr[1])
		print(result)
		box[result] -= 1
		update(1, 1, m, -1, result)
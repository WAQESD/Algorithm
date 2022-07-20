from sys import stdin
n = int(stdin.readline())
a = list(map(int, stdin.readline().split()))
b = list(map(int, stdin.readline().split()))
db = {b[i]:i for i in range(n)}
tree = [0] * (4*n)
def update(node, start, end, idx):
	if(start > idx or idx > end): return
	tree[node] += 1
	if(start != end):
		mid = (start + end) // 2
		update(node*2, start, mid, idx)
		update(node*2+1, mid+1, end, idx)

def get(node, start, end, left, right):
	if(end < left or start > right): return 0
	if(start >= left and end <= right): return tree[node]
	mid = (start + end) // 2
	return get(node*2, start, mid, left, right) + get(node*2+1, mid+1, end, left, right)

answer = 0
for i in range(n):
	now = db[a[i]]+1
	answer += get(1, 1, n, now+1, n)
	update(1, 1, n, now)
print(answer)

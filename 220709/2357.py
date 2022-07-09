from sys import stdin
import sys
import math
sys.setrecursionlimit(10**8)
n, m = map(int, stdin.readline().split())
arr = [int(stdin.readline()) for _ in range(n)]
h = math.ceil(math.log2(n)) + 1
size = 1 << h
segment = [0 for _ in range(size)]
INF = 1000000000
def init(idx, s, e):
	if s == e:
		segment[idx] = [arr[s], arr[s]]
		return segment[idx]
	mid = (s + e) // 2
	l = init(idx * 2, s, mid)
	r = init(idx * 2 + 1, mid + 1, e)
	segment[idx] = [min(l[0], r[0]), max(l[1], r[1])]
	return segment[idx]

def find(s, e, a, b, idx):
	if e < a or b < s:
		return [INF, 0]
	mid = (s + e) // 2
	if a <= s and e <= b:
		return segment[idx]
	else:
		l = find(s, mid, a, b, idx * 2)
		r = find(mid+1, e, a, b, idx * 2 + 1)
		return [min(l[0], r[0]), max(l[1], r[1])]

init(1, 0, len(arr) - 1)

for _ in range(m):
	a, b = map(int, stdin.readline().split())
	a -= 1
	b -= 1
	answer = find(0, len(arr)-1, a, b, 1)
	print(answer[0], answer[1])
from sys import stdin
import heapq
n = int(stdin.readline())
left = []
right = []
for i in range(n):
	x = int(stdin.readline())
	if len(left) == len(right): heapq.heappush(left, -x)
	else: heapq.heappush(right, x)
	if right and -left[0] > right[0]:
		r = heapq.heappop(right)
		l = -heapq.heappop(left)
		heapq.heappush(left, -r)
		heapq.heappush(right, l)
	print(-left[0])

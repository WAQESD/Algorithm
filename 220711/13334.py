from sys import stdin
import heapq
n = int(stdin.readline())
people = []
for i in range(n):
	h, o = map(int, stdin.readline().split())
	[s, e] = [min(h, o), max(h, o)]
	people.append([e, s])
people.sort()
d = int(stdin.readline())

heap = []
idx = n-1
answer = 0
for [e, s] in people:
	if(e-s>d): continue
	while heap and heap[0][0] < e-d:
		heapq.heappop(heap)
	heapq.heappush(heap, [s, e])
	answer = max(answer, len(heap))
print(answer)

from sys import stdin
import heapq
n, k = map(int, stdin.readline().split())

jewels = [0] * n
bags = [0] * k

for i in range(n): 
	jewels[i] = list(map(int, stdin.readline().split()))

heap = []
for i in range(k): bags[i] = int(stdin.readline())
bags.sort()
jewels.sort()
answer = 0
for w in bags:
	while (len(jewels) > 0 and w >= jewels[0][0]):
		heapq.heappush(heap, -jewels[0][1])
		heapq.heappop(jewels)
	
	if(len(heap) > 0):
		answer += -heapq.heappop(heap)
	elif (len(jewels) < 1): break

print(answer)
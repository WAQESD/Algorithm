from sys import stdin

n = int(stdin.readline())
cross = list(map(int, stdin.readline().split()))
left = list(map(int, stdin.readline().split()))
right = list(map(int, stdin.readline().split()))

l = 0
r = sum(right)

dist = l + r + cross[0]
idx = 1

for i in range(n-1):
	l += left[i]
	r -= right[i]
	tmp = l + r + cross[i+1]
	if(dist > tmp):
		idx = i+2
		dist = tmp

print(idx, dist)

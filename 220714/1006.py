from sys import stdin
tc = int(stdin.readline())

def solve(start, both, up, down):
	for i in range(start, n):
		both[i+1] = min(up[i]+1, down[i]+1)
		if(zone2[i] + zone1[i] <= w):
			both[i+1] = min(both[i+1], both[i]+1)
		if(i > 0 and zone2[i-1] + zone2[i] <= w and zone1[i-1] + zone1[i] <= w):
			both[i+1] = min(both[i+1], both[i-1]+2)
		if(i < n-1):
			up[i+1] = both[i+1] + 1
			if(zone1[i+1] + zone1[i] <= w):
				up[i+1] = min(up[i+1], down[i]+1)
			down[i+1] = both[i+1] + 1
			if(zone2[i+1] + zone2[i] <= w):
				down[i+1] = min(down[i+1], up[i]+1)
	return both, up, down

for _ in range(tc):
	n, w = map(int, stdin.readline().split())
	zone1 = list(map(int, stdin.readline().split()))
	zone2 = list(map(int, stdin.readline().split()))
	both = [0] * (n+1)
	up = [0] * (n+1)
	down = [0] * (n+1)
	both[0] = 0
	up[0] = 1
	down[0] = 1
	both, up, down = solve(0, both, up, down)
	result = both[n]

	if(n > 1 and zone1[0] + zone1[n-1] <= w):
		both[1] = 1
		up[1] = 2
		down[1] = 1 if zone2[0] + zone2[n-1] <= w else 2
		both, up, down = solve(1, both, up, down)
		result = min(result, down[n-1]+1)
	if(n > 1 and zone2[0] + zone2[n-1] <= w):
		both[1] = 1
		down[1] = 2
		up[1] = 1 if zone1[0] + zone1[n-1] <= w else 2
		both, up, down = solve(1, both, up, down)
		result = min(result, up[n-1]+1)
	if(n > 1 and zone1[0] + zone1[n-1] <= w and zone2[0] + zone2[n-1] <= w):
		both[1] = 0
		down[1] = 1
		up[1] = 1
		both, up, down = solve(1, both, up, down)
		result = min(result, both[n-1]+2)

	print(result)

